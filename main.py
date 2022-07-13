from Log_in import *
from Site_Functions import *

app = Flask(__name__)

app.secret_key = '42,will do for now'


@app.route('/', methods=['GET', 'POST'])
def home():
    # try to get user if fails go to log in , otherwise go to homepage
    if request.method == 'GET':
        if not session.get('user'):
            return redirect('log_in')

        # retrieve the info from the session_user, its not really needed to unpack but is for nicer html
        role = session['user']['role']
        rights = role['rights']
        buildings = role['building']
        zones = role['zones']

        # retrieve task information needed to show tasks
        tasks = DbCon(session['db']).return_result(
            'SELECT TASK_TABLE.ROWID,* FROM TASK_TABLE JOIN Zone_table ON zone = Zone_description '
            'WHERE status = "new"')

        return render_template('/home.html', tasks=tasks, rights=rights, buildings=buildings, zones=zones)

    # if there is an post request, check which form and execute the needed function from site functions
    if request.method == 'POST':
        user = session['user']
        user_name = user['name']

        if request.form.get('task_add_task'):
            add_task()

        if request.form.get('user_add'):
            site = session['user']['site']
            add_user(site)

        # to refactor and place for most part in site functions
        if request.form.get('finish_task'):
            task_id = request.form.get('finish_task')
            finished_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            DbCon(session['db']).connection_simple(f'UPDATE TASK_TABLE SET status = "finished",'
                                                   f' finished_on = "{finished_time}",'
                                                   f' finished_by = "{user_name}" '
                                                   f' where ROWID = {task_id}')

        if request.form.get('cancel_task'):
            task_id = request.form.get('cancel_task')
            DbCon(session['db']).connection_simple(f'UPDATE TASK_TABLE SET status = "Cancelled"'
                                                   f' WHERE ROWID = {task_id} ')

    return redirect('/')


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        try:
            user = login(request.form.get('username'), request.form.get('Password'))
            # save the db as a Session object
            session['db'] = f'{user.site}.db'
            # vars function transforms object to dict.
            user.role = vars(user.role)
            session['user'] = vars(user)
            return redirect('/')

        except:
            # to be replaced by a fun 'WHO ARE YOU PAGE/i'm thinking CSI MIAMI'
            return "We do not know who you are"

    if request.method == 'GET':
        return render_template('/log_in.html')


@app.route('/finished_tasks')
def finished_tasks():
    if request.method == 'GET':
        try:
            user = session['user']
        except:
            return redirect('/log_in')

        # todo replace retrieving the next info for a function
        # task information - filtered on finished
        tasks = DbCon(session['db']).return_result(
            'SELECT TASK_TABLE.ROWID,* FROM TASK_TABLE JOIN Zone_table ON zone = Zone_description '
            'WHERE status = "finished"')

        # retrieve the info from the session_user, its not really needed to unpack but is for nicer html
        role = session['user']['role']
        rights = role['rights']
        buildings = role['building']
        zones = role['zones']

        return render_template('finished_tasks.html', tasks=tasks, rights=rights, buildings=buildings, zones=zones)


@app.route('/buildings_zones', methods=['GET', 'POST'])
def building_zones():
    # check if the user is login by checking their cookies
    if not session['user']:
        return redirect('/log_in')

    # to combine in verify function within site functions
    user = session['user']
    db = session['db']

    # the local admin page used to create Buildings and Zones
    if request.method == 'GET':
        # retrieve info needed to create
        buildings = DbCon(db).unpack_first_result('SELECT * FROM BUILDINGS')
        zones = DbCon(db).return_result('SELECT ROWID,* FROM Zone_table')
        return render_template('buildings_zones.html', buildings=buildings, zones=zones)

    # it there is a post request it means either a building,role,zone or user should be added
    if request.method == 'POST':
        if request.form.get('add_building'):
            add_building(db)

        if request.form.get('delete_building'):
            building = request.form.get('delete_building')
            # delete from building main table
            DbCon(db).connection_simple(f'DELETE FROM BUILDINGS WHERE Building = "{building}" ')
            # delete from building_rights table
            DbCon(db).connection_simple(f'DELETE FROM BUILDING_RIGHTS WHERE Building = "{building}"')

        if request.form.get('add_Zone'):
            add_zone()

        if request.form.get('delete_zone'):
            zone_id = request.form.get('zone_id')
            DbCon(db).connection_simple(f'DELETE FROM Zone_table WHERE ROWID = "{zone_id}"')

        # todo to remove after implement elsewhere
        if request.form.get('role_add'):
            # inputs the user to give the site info to the role object
            add_role(user['site'])
        if request.form.get('user_add'):
            # looks a bit strange but use the site of the making user for created user
            add_user(user['site'])

        return redirect('/buildings_zones')


@app.route('/role', methods=['GET', 'POST'])
def roles_page():
    try:
        db = session['db']
        user = session['user']
    except:
        return redirect('/log_in')

    if request.method == "GET":
        # retrieve info needed to create
        buildings = DbCon(db).unpack_first_result('SELECT * FROM BUILDINGS')
        role_list = DbCon(db).unpack_first_result('SELECT role_name FROM ROLE_TABLE')
        roles = []

        for role in role_list:
            role = Role(user['site'], role)
            role.retrieve_role_information()
            # append an dict. version of the role object to the roles list
            roles.append(vars(role))

        return render_template('/roles.html', buildings=buildings, roles=roles)
    if request.method == "POST":

        if request.form.get('delete_role'):
            role = request.form.get('delete_role')
            DbCon(db).connection_simple(f'DELETE FROM ROLE_TABLE WHERE role_name = "{role}"')
            DbCon(db).connection_simple(f'DELETE FROM RIGHTS WHERE Role = "{role}"')
            DbCon(db).connection_simple(f'DELETE FROM BUILDING_RIGHTS WHERE Role = "{role}"')

        # todo change role function to no longer need user[site] as it is useless.
        #  replace with session[db],within role func
        if request.form.get('add_role'):
            add_role(user['site'])

        return redirect('/role')


@app.route('/reoccur', methods=['GET', 'POST'])
def reoccur_page():
    if request.method == 'GET':
        try:
            user = session['user']
        except:
            return redirect('/log_in')

        tasks = DbCon(session['db']).return_result(
            'SELECT reoccurring_tasks.ROWID,* FROM reoccurring_tasks JOIN Zone_table ON zone = Zone_description ')
        # retrieve the info from the session_user, its not really needed to unpack but is for nicer html
        role = session['user']['role']
        rights = role['rights']
        buildings = role['building']
        zones = role['zones']

        return render_template('reoccuring.html', tasks=tasks, rights=rights, buildings=buildings, zones=zones)


if __name__ == '__main__':
    app.run()
