def json_userCreateChild(id):
    return {
        "methodSend": "POST",
        "endPoint": "user",
        "payload": {
            "userId": id,
            "name": "Fulano",
            "usr": "usrFulanoComSenha4",
            "psw": "SenhaDoFulano4",
            "emails": [
                {
                    "email": "outroendereco@email.com",
                    "userId": "idUser001",
                    "userEmailTypeId": "personal",
                    "active": False
                },
                {
                    "email": "outroendereco2@email.com",
                    "userId": "idUser001",
                    "userEmailTypeId": "work",
                    "active": False
                }
            ],
            "phones": [
                {
                    "phone": "9876543210",
                    "userId": "idUser001",
                    "userPhoneTypeId": "personal",
                    "active": False
                },
                {
                    "phone": "9876543210987",
                    "userId": "idUser001",
                    "userPhoneTypeId": "work",
                    "active": False
                }
            ],
            "userTypeId": "user"
        }
    }
