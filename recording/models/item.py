from sqlalchemy.dialects.postgresql import UUID
from db import db
import uuid

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(UUID(as_uuid=True), db.ForeignKey("stores.id"), unique=False, nullable=False)

    store = db.relationship("StoreModel", back_populates="items")