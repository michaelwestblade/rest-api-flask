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

    if "name" not in store_data:
        abort(400, message="Missing 'name' parameter")

    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Duplicate name")

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
def create_item():
    item_data = request.get_json()

    if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
        abort(400, message="Bad request. Ensure 'price', 'store_id', and 'name' fields are present.")

    for item in items.values():
        if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
            abort(400, message="Item already exists")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
        return {"message": "store not found"}, 404

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