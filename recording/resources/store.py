from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from schemas import StoreSchema

StoreBlueprint = Blueprint('stores', __name__, description="Operations on stores")


@StoreBlueprint.route('/stores/<int:store_id>')
class Stores(MethodView):
    @StoreBlueprint.response(200, StoreSchema())
    def get(self, store_id: int):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id: int):
        store = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("DELETE not implemented")

@StoreBlueprint.route('/stores')
class StoresList(MethodView):
    @StoreBlueprint.response(200, StoreSchema(many=True))
    def get(self):
        stores = StoreModel.query.all()
        return list(stores)

    @StoreBlueprint.arguments(StoreSchema)
    @StoreBlueprint.response(201, StoreSchema())
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError as e:
            print(e)
            abort(409, message="Store already exists")
        except SQLAlchemyError as e:
            print(e)
            abort(500, message="Error adding store")

        return store, 201