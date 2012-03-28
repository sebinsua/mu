from .redirect import RedirectForm
from flaskext.wtf import TextField, PasswordField, validators

class LoginForm(RedirectForm):
    user_identity = TextField('Username or email', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])
