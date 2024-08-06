def json_userGetCollection(id):
    return {
        "methodSend": "GET",
        "endPoint": f"user/collection/{id}",
        "payload": {}
    }
