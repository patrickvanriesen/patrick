from datetime import date
import hashlib
import csv
from Role import *


# User object to store user data
class Users:
    def __init__(self, name, password, site, email, role_name):
        self.name = name
        # store a hash of the password
        key = hashlib.sha256(password.encode('utf-8'))
        self.password = key.hexdigest()
        # the site defines where you work
        self.site = site
        # the role defines the user rights
        self.role_name = role_name
        # for some users also add the Email-Account
        self.email = email
        # Creation date for users, should actually re-place this to inside the db function
        self.creation = date.today()
        # Holds the Role Object
        self.role = Role(self.site, self.role_name)

    def write_to_db(self):
        # Create a Tuple of Values to be written
        user = (self.name, self.password, self.site, self.email, self.role_name, self.creation)
        # add user to DB, db = 'SITE''.db'
        db = f'{self.site}.db'
        DbCon(db).insert('INSERT INTO USER_TABLE VALUES(?,?,?,?,?,?)', user)

    def write_userkey(self):
        with open('userkeys.csv', 'a', newline='') as u:
            writer = csv.writer(u)
            # write a key consisting of name+pass and site so we now the DB/Site to access
            writer.writerow([f'{self.name}{self.password}', f'{self.site}.db'])
