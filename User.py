from datetime import date
import hashlib
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
        # holds the global_id
        self.global_id = ''

    def write_to_db(self):
        # Create a Tuple of Values to be written
        user = (self.name, self.password, self.site, self.email, self.role_name, self.creation, self.global_id)
        # add user to DB, db = 'SITE''.db'
        db = f'{self.site}.db'
        DbCon(db).insert('INSERT INTO USER_TABLE VALUES(?,?,?,?,?,?,?)', user)

    def write_userkey(self):
        user = (self.name, self.name + self.password, f'{self.site}.db')
        print(user)
        DbCon('global_user.db').insert('INSERT INTO global_user VALUES(?,?,?)', user)
        # retrieve global_key and input into object
        global_key = DbCon('global_user.db').unpack_first_result('SELECT ROWID FROM global_user '
                                                                 f'WHERE userkey = "{self.name + self.password}"')
        self.global_id = global_key[0]
        print(self.global_id)
