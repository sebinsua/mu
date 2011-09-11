from flask import Blueprint, request, redirect, flash, render_template
bp = Blueprint('user', __name__)

@bp.route('/user/<username>')
def show_user(username):
    pass

@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        from mu.model.domain.user import UserDomain
        user_domain = UserDomain()

        if user_domain.login(request.form):
            # It would actually be better to redirect to the original page
            # we were on by passing this via request.form
            redirect("/")

    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register_user():
    from mu.form.registration import RegistrationForm
    registration_form = RegistrationForm(request.form)

    if request.method == "POST" and registration_form.validate():
        # We only need to access the UserDomain when we are passed
        # POST data with which to attempt user registration.
        from mu.model.domain.user import UserDomain
        user_domain = UserDomain()

        try:
            user_id = user_domain.register(request.form)
            user_domain.force_login(user_id)
            flash("Thanks for registering!")
            return redirect("/")
        except Error:
            # Capture particular exception messages
            # and flash these on the register page.
            flash("There has been a problem with your registration...")

    return render_template('register.html', form=registration_form)
