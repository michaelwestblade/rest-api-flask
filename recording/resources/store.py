import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from data.db import stores

StoreBlueprint = Blueprint('stores', __name__, description="Operations on stores")


@StoreBlueprint.route('/stores/<string:store_id>')
class Stores(MethodView):
    def get(self, store_id: str):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id: str):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found")

@StoreBlueprint.route('/stores')
class StoresList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
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