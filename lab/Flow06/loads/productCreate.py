def json_productCreate(id):
    return {
        "methodSend": "POST",
        "endPoint": "createProduct",
        "payload": {
            "name": "Novo Produto 5",
            "description": "Descrição do Novo Produto 5",
            "productTypeId": "product",
            "price": 0.00,
            "tags": None,
            "userId": id,
            "systemId": "sysLocacaoRoupa"
        }
    }
