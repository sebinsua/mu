from .redirect import RedirectForm
from flaskext.wtf import TextField, PasswordField, validators
from flaskext.wtf.html5 import EmailField

class RegistrationForm(RedirectForm):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
