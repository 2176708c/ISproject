
from flask import ( 
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    abort
)


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/choose')
def choose():
    return render_template('choose.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/')
def logout():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run()
