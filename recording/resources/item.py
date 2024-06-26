import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from data.db import items, stores

from schemas import ItemSchema, ItemUpdateSchema

ItemBlueprint = Blueprint('items', __name__, description="Operations on items")


@ItemBlueprint.route('/items/<string:item_id>')
class Items(MethodView):
    @ItemBlueprint.response(200, ItemSchema())
    def get(self, item_id: str):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id: str):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    @ItemBlueprint.arguments(ItemUpdateSchema)
    @ItemBlueprint.response(200, ItemSchema())
    def put(self, item_data, item_id: str):
        try:
            item = items[item_id]
            item |= item_data

            return item, 200
        except KeyError:
            abort(404, message="Item not found")

@ItemBlueprint.route('/items')
class ItemsList(MethodView):
    @ItemBlueprint.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @ItemBlueprint.arguments(ItemSchema)
    @ItemBlueprint.response(201, ItemSchema())
    def post(self, item_data):
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