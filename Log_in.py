from User import *


def login(username, password):
    # open and read through keys, if key matches the key[0] field return the db
    db = find_key(username, password)
    # check the DB for this User, Open the DB Conn, find user based on Name, Create User Object
    user_info = DbCon(db).find_user(username)
    user = Users(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])
    # initiates an empty Role object,  retrieve Role info, change to retrieve role information
    role = Role(user.site, user.role_name)
    role.retrieve_role_information()
    user.role = role

    return user


def find_key(user, pas):
    # used to return the db value of a user_key combo
    pas = hashlib.sha256(pas.encode('utf-8')).hexdigest()
    # open the csv file, and read it
    with open('userkeys.csv', newline='') as keys_csv:
        keys = csv.reader(keys_csv)
        for key in keys:
            if key[0] == user + pas:
                db = key[1]
                return db
