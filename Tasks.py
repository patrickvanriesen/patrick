from sql import *
from flask import *
from datetime import datetime


class Task:
    def __init__(self, description, responsible, role, building, zone, start_date, due_date, duration):
        # basic task info to get started, as it is always required take them all as input
        self.description = description
        self.responsible = responsible
        self.role = role
        self.building = building
        self.zone = zone
        self.start_date = start_date
        self.due_date = due_date
        self.duration = duration
        # status, status template: new > finished > verified // new > error reported > verified/back to new
        self.status = 'new'
        # Creation date-time
        self.creation = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # rescheduling info >>> maybe make redundant by adding all info to rescheduled task
        # or possibly expand
        self.reoccur = ""
        # instructions & reported issues, maybe needs special handling to properly display.
        self.instructions = ""
        self.reported_issue = ""
        self.id = ""
        self.finished_on = ''
        self.finished_by = ''
        self.verified_on = ''
        self.verified_by = ''

    def write_to_db(self):
        task_tuple = (self.description, self.responsible, self.role, self.building, self.zone,
                      self.start_date, self.due_date, self.duration, self.creation,
                      self.status, self.reoccur, self.instructions, self.reported_issue,
                      self.finished_on, self.finished_by, self.verified_on, self.finished_by)

        db = session['db']
        query = 'INSERT INTO TASK_TABLE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        DbCon(db).insert(query, task_tuple)
