from flaskext.wtf import Form, TextField, HiddenField, QuerySelectField, validators
from mu.model.entity.product import ProductType, ProductStatus, ProductMedium
from mu.model.entity.agent import AgentType

class AddProductForm(Form):
    agent = TextField('Artist')
    agent_type = HiddenField()
    content_owner = TextField('Label')
    release_date = TextField('Release Date')
    title = TextField('Title')
    type = QuerySelectField('Type',
            query_factory=lambda: ProductType.query.all())
    status = QuerySelectField('Status',
            query_factory=lambda: ProductStatus.query.all())
    medium = QuerySelectField('Medium',
            query_factory=lambda: ProductMedium.query.all())

    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        agent_type_id = AgentType.query.filter_by(name=obj['agent_type']).one().agent_type_id
        kwargs.setdefault('agent_type', agent_type_id)
        Form.__init__(self, formdata, obj, prefix, **kwargs)
