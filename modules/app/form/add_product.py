from flaskext.wtf import Form, TextField, QuerySelectField, validators
from mu.model.entity.product import ProductType, ProductStatus, ProductMedium

class AddProductForm(Form):
    artist = TextField('Artist')
    label = TextField('Label')
    release_date = TextField('Release Date')
    title = TextField('Title')
    type = QuerySelectField('Type',
            query_factory=lambda: ProductType.query.all())
    status = QuerySelectField('Status',
            query_factory=lambda: ProductStatus.query.all())
    medium = QuerySelectField('Medium',
            query_factory=lambda: ProductMedium.query.all())
