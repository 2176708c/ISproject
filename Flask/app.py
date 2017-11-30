from flask import (
                   Flask,
                   flash,
                   redirect,
                   render_template,
                   request,
                   session,
                   abort
                   )
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask.ext.login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    return (render_template('home.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/upload')
def upload():
    return (render_template('upload.html'))

@app.route('/profile')
def profile():
    return (render_template('profile.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return (render_template('home.html'))
        else:
            error= 'Invalid Credentials! Please try again'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('home.html')

@app.route('/register',  methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return (render_template('home.html'))
    return (render_template('register.html'))

@app.route('/julie')
def julie():
    return (render_template('julie.html'))


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

