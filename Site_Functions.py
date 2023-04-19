import datetime
from datetime import timedelta
from User import *
from Tasks import *
from reoccuring_tasks import add_reoccurring_task


def convert_date(wrong_date):
    # correct later, for now is not working with edit modal
    # try:
    # wrong_date = datetime.strptime(wrong_date, "%Y-%m-%d")
    # correct_date = datetime.strftime(wrong_date, "%d-%m-%Y")
    # except:
    correct_date = wrong_date
    return correct_date


# a lot of to do here as it all needs to be based on site inputs
def add_role(site):
    role = Role(site, request.form.get('role_name'))
    role.rights = request.form.getlist('role_rights')
    # each role should also have rights to itself, otherwise OPS could not see OPS
    role.rights.append(role.role_name)
    role.building = request.form.getlist('role_building')
    restricted = request.form.get('role_restricted')
    if restricted == 'TRUE':
        role.restricted = request.form.get('role_restricted')
    role.write_to_db()


def add_user(site):
    user = Users(request.form.get('user_name'), request.form.get('user_password'), site,
                 request.form.get('user_email'), request.form.get('user_role'))
    user.write_userkey()
    user.write_to_db()


def add_building(db):
    # simplifies main.py by retrieving all info from form on post req. and adding to db
    building = request.form.get('add_building')
    DbCon(db).add_building(building)


def add_zone():
    # simplifies main.py by retrieving all info from form on post req. and adding to db
    db = session['db']
    zone_building = request.form.get('add_zone_building')
    zone_header = request.form.get('add_zone_header')
    zone_desc = request.form.get('add_zone_description')
    zone_color = request.form.get('add_zone_color')

    query = "INSERT INTO Zone_table VALUES (?,?,?,?)"
    DbCon(db).insert(query, (zone_building, zone_header, zone_desc, zone_color))


def add_task():
    # retrieves all info from html form and inputs it in db
    # define the variables for cleaner input of task object
    description = request.form.get('task_description')
    responsible = request.form.get('task_responsible')
    role = request.form.get('task_role')
    building = request.form.get('task_building')
    zone = request.form.get('task_zone')
    duration = request.form.get('task_duration')
    start = convert_date(request.form.get('task_start_date'))
    due = convert_date(request.form.get('task_due_date'))

    # define task object and add the following to it : instructions, Re-occur settings
    task = Task(description, responsible, role, building, zone, start, due, duration)
    task.instructions = request.form.get('task_instruction')
    task.reoccur = request.form.get('task_reoccur')

    # re-occuring tasks
    if int(task.reoccur) > 0:
        # if higher then one call add_reoccuring_task
        re_occur_settings = (request.form.get('exclude_wk'), request.form.get('exclude_wday'))
        add_reoccurring_task(task, re_occur_settings)

    # write task to db
    task.write_to_db()


def filter_tasks(query):
    # retrieve info from form fields
    filter_column = request.args.get('filter_column')
    filter_type = request.args.get('filter_type')
    filter_value = request.args.get('filter_value')
    # transform deviating values
    if filter_column == 'department':
        filter_column = 'role'
    # create an where clause with filters
    where = ''
    if filter_type == 'contains':
        where = f'{filter_column} like "%{filter_value}%"'
    if filter_type == 'equals':
        where = f'{filter_column} = "{filter_value}"'
    if filter_type == 'starts with':
        where = f'{filter_column} like "{filter_value}%"'
    if filter_type == 'ends with':
        where = f'{filter_column} like "%{filter_value}"'
    query = f'{query} AND {where}'
    return query


def sort_tasks(query):
    # retrieve info from arguments
    sort_column = request.args.get('sort_column')
    sort_value = request.args.get('sort_value')
    # change incorrect data
    if sort_column == 'department':
        sort_column = 'role'
    if sort_value == 'Descending':
        sort_value = 'DESC'
    if sort_value == 'Ascending':
        sort_value = 'ASC'
    order_by = f'ORDER BY {sort_column} {sort_value}'
    query = query + order_by
    return query


def check_user_login():
    user = session['user']
    role = session['user']['role']
    rights = role['rights']
    buildings = role['building']
    zones = role['zones']
    return user, role, rights, buildings, zones


def filter_tasks_on_rights(tasks, rights):
    counter = 0
    for task in tasks:
        if task[3] not in rights:
            tasks.pop(counter)
        counter += 1
    return tasks


def create_re_occuring_tasks():
    reoccuring_tasks = DbCon(session['db']).return_result('SELECT ROWID,* FROM REOCCURRING_TASKS')
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    day_of_week = datetime.today().weekday()
    for t in reoccuring_tasks:
        # transform last creation to date-time object
        last_creation = datetime.strptime(t[13], '%d-%m-%Y %H:%M:%S')
        # find re-occur timer in days
        days = int(t[10])
        # add last-creation and days and compare to today
        last_creation += timedelta(days=days)
        if last_creation <= datetime.today():
            # if in weekend skip this and exclude weekend is true skip
            if day_of_week >= 5 and t[11] == True:
                continue
            # if in weekday and exclude wkday is true then skip
            if day_of_week < 5 and t[12] == True:
                continue
            task = Task(t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8])
            task.reoccur = days
            task.write_to_db()
            DbCon(session['db']).connection_simple(f'update REOCCURRING_TASKS set last_creation = "{now}" '
                                                   f'where ROWID = "{t[0]}"')
