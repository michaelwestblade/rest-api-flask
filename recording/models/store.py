from sqlalchemy.dialects.postgresql import UUID
from db import db
import uuid

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship('ItemModel', back_populates='store', lazy='dynamic')