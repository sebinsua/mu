from helper.database import db

from mu.model.entity.event import Event
from mu.model.entity.work import Work

from datetime import datetime

class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key=True)
    work_id = db.Column(db.Integer, db.ForeignKey('Work.work_id'))
    product_type_id = db.Column(db.Integer, db.ForeignKey('ProductType.product_type_id'), nullable=False)
    product_status_id  = db.Column(db.Integer, db.ForeignKey('ProductStatus.product_status_id'), nullable=False)
    product_medium_id = db.Column(db.Integer, db.ForeignKey('ProductMedium.product_medium_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.event_id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    sort_title = db.Column(db.String(50))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    work = db.relationship('Work', uselist=False, \
            backref=db.backref('Product', lazy='dynamic'))
    product_type = db.relationship('ProductType', uselist=False, \
            backref=db.backref('Product', lazy='dynamic'))
    product_status = db.relationship('ProductStatus', uselist=False, \
            backref=db.backref('Product', lazy='dynamic'))
    product_medium = db.relationship('ProductMedium', uselist=False, \
            backref=db.backref('Product', lazy='dynamic'))
    event = db.relationship('Event', uselist=False, \
            backref=db.backref('Product', lazy='dynamic', uselist=False))

    def __init__(self, title, event_id, product_type_id=None, \
            product_status_id=None, product_medium_id=None, work_id=None):
        self.work_id = work_id
        self.product_type_id = product_type_id
        self.product_status_id = product_status_id
        self.event_id = event_id
        self.title = title
        self.sort_title = title[:50]

class ProductMedium(db.Model):
    __tablename__ = 'ProductMedium'
    product_medium_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductMedium %r>' % self.name

class ProductType(db.Model):
    __tablename__ = 'ProductType'
    product_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductType %r>' % self.name

class ProductStatus(db.Model):
    __tablename__ = 'ProductStatus'
    product_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductStatus %r>' % self.name
