
from sql import *

zone_query = f'SELECT Zone_description,Zone_Color FROM Zone_table WHERE Building IN ' \
                     f'(SELECT Building FROM BUILDING_RIGHTS WHERE Role = "SV")'

zones = DbCon('KBL.db').return_result(zone_query)
print(zones)
