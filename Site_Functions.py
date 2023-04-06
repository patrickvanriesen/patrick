from User import *
from Tasks import *
from reoccuring_tasks import add_reoccurring_task


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
    user.write_to_db()
    user.write_userkey()


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
    start = request.form.get('task_start_date')
    due = request.form.get('task_due_date')

    # define task object and add the following to it : instructions Re-occur settings
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
    print(where)
    print(f'{query} AND {where}')
    query = f'{query} AND {where}'
    return query
