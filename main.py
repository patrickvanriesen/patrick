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
        return render_template('/home.html', rights=rights, buildings=buildings, zones=zones)

    # if there is an post request, check which form and execute the needed function from site functions
    if request.method == 'POST':
        if request.form.get('task_add_task'):
            add_task()
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


# todo this page will be either changed or removed
@app.route('/local_admin', methods=['GET', 'POST'])
def local_admin():
    # check if the user is login by checking their cookies
    if not session['user']:
        return redirect('/log_in')

    # to combine in verify function within site functions
    user = session['user']
    db = session['db']

    if user['role']['role_name'] != "Local_admin":
        return 'You do not have access'

    # the local admin page used to create Building , Roles and users
    if request.method == 'GET':
        # retrieve info needed to create roles/users (user the rights list also for roles)
        buildings = DbCon(db).unpack_first_result('SELECT * FROM BUILDINGS')
        rights = DbCon(db).unpack_first_result('SELECT role_name from ROLE_TABLE')
        return render_template('Local_Admin.html', buildings=buildings, rights=rights)

    # it there is a post request it means either a building,role,zone or user should be added
    if request.method == 'POST':
        if request.form.get('add_building'):
            add_building(db)

        if request.form.get('role_add'):
            # inputs the user to give the site info to the role object
            add_role(user['site'])

        if request.form.get('user_add'):
            # looks a bit strange but use the site of the making user for created user
            add_user(user['site'])

        return redirect('/local_admin')


if __name__ == '__main__':
    app.run()
