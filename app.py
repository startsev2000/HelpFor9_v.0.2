import flask

from flask import redirect, request
from flask_admin.contrib.sqla import ModelView
from flask_admin.helpers import is_safe_url
from flask_login import login_user, logout_user, login_required

from conf import *

from models import *
import hashlib

admin.add_view(ModelView(User, db.session))


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return 'HELLO'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = request.form
    print(request.form)
    password = hashlib.sha256()
    password.update(str(form['password']).encode('utf-8'))
    password = str(password.hexdigest())
    user = User.query.filter_by(email=str(form['email']),
                                password=password).all()
    user = None
    if user:
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run()
