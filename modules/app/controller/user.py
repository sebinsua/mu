from flask import Blueprint, request, redirect, flash, render_template
from mu.model.domain.user import UserDomain

bp = Blueprint('user', __name__)
user_domain = UserDomain()

@bp.route('/user/<username>')
def show_user(username):
    pass

@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    from mu.form.login import LoginForm
    login_form = LoginForm(request.form)

    if request.method == "POST" and login_form.validate():
        user_identity = request.form.get('user_identity')
        password = request.form.get('password')

        try:
            if user_domain.login(user_identity, password):
                # TODO: It would actually be better to redirect to the original page
                # we were on by passing this via request.form
                return redirect("/")
            else:
                flash("This does not match the account's password", "error")
        except Exception, e:
            flash(e, "error")

    return render_template('login.html', form=login_form)

@bp.route('/logout')
def logout_user():
    user_domain.logout()
    return redirect('/')

@bp.route('/register', methods=['GET', 'POST'])
def register_user():
    from mu.form.registration import RegistrationForm
    registration_form = RegistrationForm(request.form)

    if request.method == "POST" and registration_form.validate():
        # We only need to access the UserDomain when we are passed
        # POST data with which to attempt user registration.
        email = request.form.get('email')
        username = request.form.get('username', default=email)
        password = request.form.get('password')

        try:
            user_id = user_domain.register(email, username, password, force_login=True)
            flash("Thanks for registering!", "success")
            return redirect("/")
        except Exception, e:
            # Capture particular exception messages
            # and flash these on the register page.
            flash(e, "error")

    return render_template('register.html', form=registration_form)
