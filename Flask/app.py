from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tracking')
def tracking():
    return render_template('tracking.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/compete')
def compete():
    return render_template('compete.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

if __name__ == "__main__":
    app.run()
