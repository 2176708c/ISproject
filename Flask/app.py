from flask import (
                   Flask,
                   flash,
                   redirect,
                   render_template,
                   request,
                   session,
                   abort,
                   url_for
                   )
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return (render_template('home.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      unique_filename = str(uuid.uuid4()) + ".gpx"
      f.save("static/gpx/" + secure_filename(unique_filename))
      return show()

@app.route('/upload')
def upload():
    return (render_template('upload.html'))

@app.route('/show')
def show():
    return (render_template('show.html', value = url_for('static', filename='gpxcycling.gpx')))

@app.route('/profile')
def profile():
    return (render_template('profile.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        POST_USERNAME = request.form['username']
        POST_PASSWORD = request.form['password']

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()
        if result:
            session['logged_in'] = True
            return (render_template('home.html'))
        else:
            error = 'wrong password!'
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
