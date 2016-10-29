from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():

    name = request.form['user_name']
    email = request.form['user_mail']

    print name, email

    return redirect(url_for('home'))
