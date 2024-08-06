def json_userCreateInitial():
    return {
        "methodSend": "POST",
        "endPoint": "user",
        "payload": {
            "name": "Ciclano",
            "usr": "usrCiclanoComSenha3",
            "psw": "SenhaDoCiclano3",
            "emails": [
                {
                    "email": "endereco@email.com",
                    "userId": "idAdmin000",
                    "userEmailTypeId": "others",
                    "active": True
                },
                {
                    "email": "endereco2@email.com",
                    "userId": "idAdmin000",
                    "userEmailTypeId": "others",
                    "active": True
                }
            ],
            "phones": [
                {
                    "phone": "12489156131",
                    "userId": "idAdmin000",
                    "userPhoneTypeId": "others",
                    "active": True
                },
                {
                    "phone": "1248915613123465",
                    "userId": "idAdmin000",
                    "userPhoneTypeId": "others",
                    "active": True
                }
            ],
            "userTypeId": "admin"
        }
    }
