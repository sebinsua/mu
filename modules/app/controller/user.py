from flask import Blueprint, request, redirect, flash, render_template
from mu.model.domain.user import UserDomain, AccountNotUnique

bp = Blueprint('user', __name__)

@bp.route('/user/<username>')
def profile(username):
    pass


@bp.route('/login', methods=['GET', 'POST'])
def login():
    from mu.form.login import LoginForm

    login_form = LoginForm(formdata=request.form, obj={
        'next': request.referrer if request.referrer else None
    })

    if request.method == "POST" and login_form.validate():
        user_identity = request.form.get('user_identity')
        password = request.form.get('password')

        try:
            if UserDomain.login(user_identity, password):
                return login_form.redirect('home.show_home', force_endpoint=True)
            else:
                flash("There are no accounts with this username and password.", "error")
                return login_form.redirect('user.login', force_endpoint=True)
        except Exception, e:
            flash(e, "error")

    return render_template('login.html', form=login_form)


@bp.route('/logout')
def logout():
    UserDomain.logout()
    redirect_url = request.headers.get('HTTP_REFERER')
    return redirect(redirect_url) if redirect_url else redirect('/')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    from mu.form.registration import RegistrationForm

    registration_form = RegistrationForm(request.form, obj={
        'next': request.referrer if request.referrer else None
    })

    if request.method == "POST" and registration_form.validate():
        # We only need to access the UserDomain when we are passed
        # POST data with which to attempt user registration.
        email = request.form.get('email')
        username = request.form.get('username', default=email)
        password = request.form.get('password')

        try:
            user_id = UserDomain.register(email, username, password, force_login=True)
            # flash("Thanks for registering!", "success")
            return registration_form.redirect('home.show_home', True)
        except AccountNotUnique, e:
            flash("An account already exists with these details.", "error")
            return registration_form.redirect("user.register", True)

    return render_template('register.html', form=registration_form)
