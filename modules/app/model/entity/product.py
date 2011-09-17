from helper.database import db

from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    work_id = db.Column(db.Integer,
            db.ForeignKey('works.work_id'))
    product_type_id = db.Column(db.Integer, \
            db.ForeignKey('producttypes.product_type_id'))
    product_status_id  = db.Column(db.Integer, \
            db.ForeignKey('productstatuses.product_status_id'))
    event_id = db.Column(db.Integer, \
            db.ForeignKey('events.event_id'))
    title = db.Column(db.Text, nullable=False)
    sort_title = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    work = db.relationship('Work', \
            backref=db.backref('products', lazy='dynamic')
    product_type = db.relationship('ProductType', \
            backref=db.backref('products', lazy='dynamic'))
    product_status = db.relationship('ProductStatus', \
            backref=db.backref('products', lazy='dynamic'))
    event = db.relationship('Event', \
            backref=db.backref('products', lazy='dynamic'))

    def __init__(self, work_id=None, product_type_id, product_status_id=None, \
        event_id=None, title):
        self.work_id = work_id
        self.product_type_id = product_type_id
        self.product_status_id = product_status_id
        self.event_id = event_id
        self.title = title
        self.sort_title = title # TODO: get a substring of this.

class ProductMedium(db.Model):
    __tablename__ = 'productmediums'
    product_medium_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductMedium %r>' % self.name

class ProductType(db.Model):
    __tablename__ = 'producttypes'
    product_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductType %r>' % self.name

class ProductStatus(db.Model):
    __tablename__ = 'productstatuses'
    product_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ProductStatus %r>' % self.name
