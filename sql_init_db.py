from User import *


def create_site(site):
    # call this function to create a new site, is just simply executes all the query's without returning a result
    # all sites are stored in their own database (db)
    db = f'{site}.db'
    db = DbCon(db)

    # used for storing buildings like a helper table
    db.connection_simple('CREATE TABLE BUILDINGS (Building VARCHAR(255))')
    # defines which role has rights to which department
    db.connection_simple('CREATE TABLE RIGHTS (Role VARCHAR(255) ,Right VARCHAR(255))')
    # defines which buildings the role has access to
    db.connection_simple('CREATE TABLE BUILDING_RIGHTS (Role VARCHAR(255), Building VARCHAR(255))')

    # complexer query's are stored in files
    with open('Create_User_Table.SQL') as query_file:
        query = query_file.read()
    db.connection_simple(query)

    with open('Create_Role_Table.SQL') as query:
        query = query.read()
    db.connection_simple(query)

    with open('Create_task_table.SQL') as query:
        query = query.read()
    db.connection_simple(query)

    with open('Create_Zone_table.SQL') as query:
        query = query.read()
    db.connection_simple(query)

    with open('CREATE_REOCC_TASK_TABLE.SQL') as query:
        query = query.read()
    db.connection_simple(query)

    # auto-adds an admin user for each site
    user = Users(f'{site}_admin', '42, will do', site, '', 'Local_admin')
    user.write_to_db()
    user.write_userkey()
