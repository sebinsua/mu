from flaskext.wtf import Form, TextField, SelectField, validators

class AddProductForm(Form):
    content_author = TextField('Artist')
    content_owner = TextField('Label')
    event_release_date = TextField('Date')
    product_title = TextField('Title')
    product_type = SelectField('Type')
    product_status = SelectField('Status')
    product_medium = SelectField('Medium')
