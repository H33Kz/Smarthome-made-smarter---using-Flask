from distutils.log import debug
from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/humi')
def humi():
    return render_template('humi.html')


@app.route('/controls')
def controls():
    return render_template('controls.html')


@app.route('/alerts')
def alerts():
    return render_template('alerts.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)