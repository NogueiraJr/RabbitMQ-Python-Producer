from loads.userInitial import json_userInitial
from loads.userChild import json_userChild

def payload(id, seq, connection):
    if seq == 0:
        return json_userInitial()
    elif seq == 1:
        return json_userChild(id)
    else:
        connection.close()
        return None
