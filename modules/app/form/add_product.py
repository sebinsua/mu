from flaskext.wtf import Form, TextField, HiddenField, QuerySelectField, validators
from sqlalchemy.orm.exc import NoResultFound
from mu.model.entity.product import ProductType, ProductStatus, ProductMedium
from mu.model.entity.agent import AgentType

class AddProductForm(Form):
    agent = TextField('Artist')
    type = HiddenField()
    agent_type = HiddenField()
    content_owner = TextField('Label')
    release_date = TextField('Release Date')
    title = TextField('Title')
    type = QuerySelectField('Type',
        query_factory=lambda: ProductType.query.order_by(ProductType.sequence).all())
    status = QuerySelectField('Status',
        query_factory=lambda: ProductStatus.query.order_by(ProductStatus.sequence).all())
    medium = QuerySelectField('Medium',
        query_factory=lambda: ProductMedium.query.order_by(ProductMedium.sequence).all())

    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        agent_type_id = AgentType.query.filter_by(name=obj['agent_type']).one().agent_type_id
        kwargs.setdefault('agent_type', agent_type_id)

        Form.__init__(self, formdata, obj, prefix, **kwargs)

class AddProductTypeForm(AddProductForm):
    type = HiddenField()

    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        try:
            product_type_id = ProductType.query.filter_by(name=obj['product_type']).one().product_type_id
            kwargs.setdefault('type', product_type_id)
        except NoResultFound:
            pass

        AddProductForm.__init__(self, formdata, obj, prefix, **kwargs)
