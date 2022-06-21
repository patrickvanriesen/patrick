from Tasks import *


def add_reoccurring_task(task, reoccursettings):
    db = session['db']

    reoccur_tuple = (task.description, task.responsible, task.role, task.building, task.zone,
                     task.start_date, task.due_date, task.duration, task.instructions,
                     task.reoccur, reoccursettings[0], reoccursettings[1])

    DbCon(db).insert(f"INSERT INTO REOCCURRING_TASKS VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", reoccur_tuple)
