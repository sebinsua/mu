from helper.database import db, ConstraintsMixin
from sqlalchemy.ext.associationproxy import association_proxy

from datetime import datetime

class ContentOwner(db.Model, ConstraintsMixin):
    __tablename__ = 'ContentOwner'
    content_owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    sort_name = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    __table_args__ = ( db.UniqueConstraint('name', 'start_date', 'end_date'), )

    products = association_proxy('ContentOwnerProduct', 'product')

    def __init__(self, name, start_date=None, end_date=None):
        self.name = name
        self.sort_name = name[:50]
        self.start_date = start_date
        self.end_date = end_date


class ContentOwnerProductType(db.Model):
    __tablename__ = 'ContentOwnerProductType'
    content_owner_product_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    sequence = db.Column(db.Integer)

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def __repr__(self):
        return '<ContentOwnerProductType %r>' % self.name


class ContentOwnerProduct(db.Model):
    __tablename__ = 'ContentOwnerProduct'
    content_owner_product_id = db.Column(db.Integer, primary_key=True)
    content_owner_id = db.Column(db.Integer, db.ForeignKey('ContentOwner.content_owner_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), nullable=False)
    content_owner_product_type_id = db.Column(db.Integer,
        db.ForeignKey('ContentOwnerProductType.content_owner_product_type_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    content_owner = db.relationship('ContentOwner', uselist=False,
        backref=db.backref('ContentOwnerProduct', lazy='dynamic'))
    product = db.relationship('Product', uselist=False,
        backref=db.backref('ContentOwnerProduct', lazy='dynamic'))
    content_owner_product_type = db.relationship('ContentOwnerProductType',
        uselist=False, backref=db.backref('ContentOwnerProductType', lazy='dynamic'))

    def __init__(self, content_owner_id, product_id,
                 content_owner_product_type_id=None):
        self.content_owner_id = content_owner_id
        self.product_id = product_id
        self.content_owner_product_type_id = content_owner_product_type_id
