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
    path = "static/gpx/"
    Session = sessionmaker(bind=engine)
    s = Session()
    files = s.query(File).all()
    routes = os.listdir(path)
    return (render_template('home.html', routes = routes,files = files))

@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        unique_filename = str(uuid.uuid4()) + ".gpx"
        TITLE = request.form['title']
        
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        file = File(TITLE, unique_filename)
        session.add(file)
        # commit the record the database
        session.commit()
        f.save("static/gpx/" + secure_filename(unique_filename))
        return (home())

@app.route('/upload')
def upload():
    return (render_template('upload.html'))

@app.route('/show/<file>')
def show(file):
    Session = sessionmaker(bind=engine)
    s = Session()
    f = s.query(File).filter_by(filename=file).first_or_404()
    fn = f.filename
    return render_template('show.html', value=fn)
    #file_url = url_for('static', filename=('gpx/' + file))
#return (render_template('show.html', value = file_url))

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
        USERNAME = request.form['username']
        PASSWORD = request.form['password']

        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        user = User(USERNAME, PASSWORD)
        session.add(user)
        # commit the record the database
        session.commit()

        return (render_template('home.html'))
    return (render_template('register.html'))

@app.route('/julie')
def julie():
    return (render_template('julie.html'))


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
