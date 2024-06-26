import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

ItemBlueprint = Blueprint('items', __name__, description="Operations on items")


@ItemBlueprint.route('/items/<int:item_id>')
class Items(MethodView):
    @ItemBlueprint.response(200, ItemSchema())
    def get(self, item_id: str):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id: str):
        item = ItemModel.query.get_or_404(item_id)
        try:
            db.session.delete(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(e)
            abort(500)

    @ItemBlueprint.arguments(ItemUpdateSchema)
    @ItemBlueprint.response(200, ItemSchema())
    def put(self, item_data, item_id: int):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data['price']
            item.name = item_data['name']
        else:
            item = ItemModel(id=item_id, **item_data)

        try:
            db.session.add(item)
            db.session.commit()
            return item
        except IntegrityError as e:
            print(e)
            db.session.rollback()
            abort(400)
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            abort(500)

@ItemBlueprint.route('/items')
class ItemsList(MethodView):
    @ItemBlueprint.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @ItemBlueprint.arguments(ItemSchema)
    @ItemBlueprint.response(201, ItemSchema())
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Item already exists")
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            abort(500, message="An error occurred. Please try again.")

        return item, 201
