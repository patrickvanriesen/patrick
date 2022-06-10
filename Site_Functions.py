from User import *
from Tasks import *


# a lot of to do here as it all needs to be based on site inputs
def add_role(site):
    role = Role(site, request.form.get('role_name'))
    role.rights = request.form.getlist('rights')
    # each role should also have rights to itself
    role.rights.append(role.role_name)
    role.building = request.form.getlist('role_building')
    role.write_to_db()


def add_user(site):
    user = Users(request.form.get('user_name'), request.form.get('user_password'), site,
                 request.form.get('user_email'), request.form.get('user_role'))
    user.write_to_db()
    user.write_userkey()


def add_building(db):
    building = request.form.get('add_building')
    DbCon(db).add_building(building)


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

    # write task to db
    task.write_to_db()
