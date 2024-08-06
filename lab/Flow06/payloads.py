from loads.userCreateInitial import json_userCreateInitial
from loads.userCreateChild import json_userCreateChild
from loads.userGetCollection import json_userGetCollection

def payload(id, seq, connection):
    if seq == 0:
        return json_userCreateInitial()
    elif seq == 1:
        return json_userCreateChild(id)
    elif seq == 2:
        return json_userGetCollection(id)
    else:
        connection.close()
        return None
