from sql import *


class Role:
    # used to contain all the user rights,buildings etc i think i can remove here and change db to session['db']
    def __init__(self, site, role_name):
        self.site = site
        self.building = []
        self.role_name = role_name
        # reading and writing rights, place in array as : [SV,OPS,ETC]
        self.rights = []
        # stores zone info as tuples (zone_description , zone_color)
        self.zones = []
        # define is this role gets full site Access, maybe change how this functions works
        self.restricted = False

    # Save the role object to db after all info has been filled in by add_role function
    def write_to_db(self):
        db = f'{self.site}.db'
        # insert into key table
        role = (self.role_name, self.restricted)
        DbCon(db).insert('INSERT INTO ROLE_TABLE VALUES(?,?)', role)
        # write all the rights in right list to sep. db rows
        for right in self.rights:
            right_tuple = (self.role_name, right)
            DbCon(db).insert('INSERT INTO RIGHTS VALUES(?,?)', right_tuple)
        # same as above but for building
        for building in self.building:
            building_tuple = (self.role_name, building)
            DbCon(db).insert('INSERT INTO BUILDING_RIGHTS VALUES(?,?)', building_tuple)

    def retrieve_role_information(self):
        # functions fills in the list
        # this functions will find all info in the db based on the role name
        db = f'{self.site}.db'
        # Retrieve Restriction / check if works for this function otherwise change back
        restriction_query = f'SELECT restricted FROM ROLE_TABLE WHERE role_name = "{self.role_name}"'
        self.restricted = DbCon(db).unpack_first_result(restriction_query)
        # retrieve Rights stored as a list
        rights_query = f'SELECT Right FROM RIGHTS WHERE Role = "{self.role_name}" '
        self.rights = DbCon(db).unpack_first_result(rights_query)
        # Retrieve Buildings, to update this one to look in to the rights instead of role name
        building_query = f'SELECT Building FROM BUILDING_RIGHTS WHERE Role = "{self.role_name}"'
        self.building = DbCon(db).unpack_first_result(building_query)
        # retrieve all the Zone info. (Zone_description, Zone_Color)
        # assume everyone who has access to a building has access to a zone
        zone_query = f'SELECT * FROM Zone_table WHERE Building IN ' \
                     f'(SELECT Building FROM BUILDING_RIGHTS WHERE Role = "{self.role_name}")'
        self.zones = DbCon(db).return_result(zone_query)
