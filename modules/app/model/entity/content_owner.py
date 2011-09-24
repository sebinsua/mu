from helper.database import db

from datetime import datetime

class ContentOwner(db.Model):
    __tablename__ = 'ContentOwners'
    content_owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    sort_name = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, name, start_date=None, end_date=None):
        self.name = name
        self.sort_name = name[:50]
        self.start_date = start_date
        self.end_date = end_date

class ContentOwnerProductType(db.Model):
    __tablename__ = 'ContentOwnerProductTypes'
    content_owner_product_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ContentOwnerProductType %r>' % self.name

class ContentOwnerProducts(db.Model):
    __tablename__ = 'ContentOwnerProducts'
    content_owner_product_id = db.Column(db.Integer, primary_key=True)
    content_owner_id = db.Column(db.Integer, \
            db.ForeignKey('ContentOwners.content_owner_id'), nullable=False)
    product_id = db.Column(db.Integer, \
            db.ForeignKey('Products.product_id'), nullable=False)
    content_owner_product_type_id = db.Column(db.Integer, \
            db.ForeignKey('ContentOwnerProductTypes.content_owner_product_type_id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    content_owner = db.relationship('ContentOwners', \
            backref=db.backref('ContentOwnerProducts', lazy='dynamic'))
    product = db.relationship('Products', \
            backref=db.backref('ContentOwnerProducts', lazy='dynamic'))
    content_owner_product_type = db.relationship('ContentOwnerProductType', \
            backref=db.backref('ContentOwnerProductTypes', lazy='dynamic'))

    def __init__(self, content_owner_id, product_id, \
            content_owner_product_type_id=None):
        self.content_owner_id = content_owner_id
        self.product_id = product_id
        self.content_owner_product_type_id = content_owner_product_type_id
