def payload(id, seq, connection):
    common_payload = {
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

    if seq == 0:
        return common_payload
    elif seq == 1:
        return {
            "payload": {
                # "id": id,
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
    else:
        # connection.close()
        return None
