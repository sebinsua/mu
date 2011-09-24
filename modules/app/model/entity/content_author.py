from helper.database import db

from datetime import datetime

class ContentAuthor(db.Model):
    __tablename__ = 'ContentAuthors'
    content_author_id = db.Column(db.Integer, primary_key=True)
    musicbrainz_mbid = db.Column(db.String(36))
    name = db.Column(db.Text, nullable=False)
    sort_name = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, name, musicbrainz_mbid=None, \
        start_date=None, end_date=None):
        self.musicbrainz_mbid = musicbrainz_mbid
        self.name = name
        self.sort_name = name[:50]
        self.start_date = start_date
        self.end_date = end_date

class ContentAuthorProducts(db.Model):
    content_author_product_id = db.Column(db.Integer, primary_key=True)
    content_author_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    content_author_product_type_id = db.Column(db.Integer)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, content_author_id, product_id, \
            content_author_product_type_id=None):
        self.content_author_id = content_author_id
        self.product_id = product_id
        self.content_author_product_type_id = content_author_product_type_id

class ContentAuthorProductType(db.Model):
    __tablename__ = 'ContentAuthorProductTypes'
    content_author_product_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<ContentAuthorProductType %r>' % self.name
