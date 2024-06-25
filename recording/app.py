import random
import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/stores")
def create_store():
    store_data = request.get_json()
    store_identifier = uuid.uuid4().hex
    new_store = {"id": store_identifier, "name": store_data["name"], "items": []}
    stores[store_identifier] = new_store

    return new_store, 201

@app.get("/stores/<string:id>")
def get_store(id: str):
    try:
        return stores[id]
    except KeyError:
        abort(404, message="Store not found")

@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}

@app.post("/items")
def create_item(id: str):
    item_data = request.get_json()

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
        return {"message": "store not found"}, 404

    store = stores[id]

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}

    items[item_id] = new_item

    return new_item, 201

@app.get("/items/<string:id>")
def get_item(id: str):

    try:
        return items[id]
    except KeyError:
        abort(404, message="Item not found")