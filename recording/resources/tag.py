from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel, ItemModel
from schemas import TagSchema, TagAndItemSchema

TagBlueprint = Blueprint('tag', __name__, description="Operations on tags")

@TagBlueprint.route('/stores/<int:store_id>/tags')
class StoreTags(MethodView):
    @TagBlueprint.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.tags.all()

    @TagBlueprint.arguments(TagSchema)
    @TagBlueprint.response(200, TagSchema)
    def post(self, tag_data, store_id):
        if TagModel.query.filter(TagModel.store_id == store_id, TagModel.name == tag_data["name"]).first():
            abort(409, message='Tag already exists')

        tag = TagModel(**tag_data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            abort(500, message=e)

        return tag

@TagBlueprint.route('/items/<int:item_id>/tags/<int:tag_id>')
class LinkTagsToItems(MethodView):
    @TagBlueprint.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            abort(500, message=e)

        return tag

    @TagBlueprint.response(200, TagSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            abort(500, message=e)

        return tag

@TagBlueprint.route("/tags/<int:tag_id>")
class Tag(MethodView):
    @TagBlueprint.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @TagBlueprint.response(202, TagSchema, description="Delete a tag if no item is tagged with it", example={"message": "Tag deleted"})
    @TagBlueprint.alt_response(404, description="Tag not found")
    @TagBlueprint.alt_response(400, description="Returned if the tag is assigned to one or more items")
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items:
            try:
                db.session.delete(tag)
                db.session.commit()
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback()
                abort(500, message=e)

        abort(400, message="Tag is assigned to one or more items")

