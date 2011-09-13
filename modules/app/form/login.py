from flaskext.wtf import Form, TextField, PasswordField, validators

class LoginForm(Form):
    user_identity = TextField('Username or Email', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])
