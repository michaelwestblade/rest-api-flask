import random

from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "id": 1,
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/stores")
def get_stores():
    return {"stores": stores}


@app.post("/stores")
def create_store():
    request_data = request.get_json()
    new_store = {id: random.randint(1, 10000), "name": request_data["name"], "items": []}
    stores.append(new_store)

    return new_store, 201

@app.get("/stores/<int:id>")
def get_store(id):
    for store in stores:
        if store["id"] == id:
            return store, 200

    return {"message": "store not found"}, 404

@app.post("/stores/<int:id>/items")
def create_item(id):
    request_data = request.get_json()
    for store in stores:
        if store["id"] == id:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)

            return new_item, 201

    return {"message": "store not found"}, 404
