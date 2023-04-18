from Site_Functions import *

DbCon('KBL.db').connection_simple(f'UPDATE TASK_TABLE SET status = "Verified" WHERE status = "Completed"')
