import json
import uuid

import hyperwallet

from flask import Flask, render_template, request, redirect, url_for

api = hyperwallet.Api(
    "restapiuser@5046781612",
    "Password1$",
    "prg-15cefcdc-2363-4bf0-ab3e-b7d9959bcdd7",
    "https://api.sandbox.hyperwallet.com"
)

user = {}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('profile.html')


@app.route('/add_bank')
def add_bank():
    return render_template('add_bank.html', name = user["firstName"])


@app.route('/transfer')
def transfer():
    return render_template('transfer_method.html', token = user["token"])


@app.route('/create_transfer_method', methods=['POST'])
def create_transfer_method():

    headers = {"Json-Cache-Token": request.form['hw_json_cache_trm_token']}

    response = api.createTransferMethod(user["token"], {}, headers)

    return redirect(url_for('home'))


@app.route('/create_user', methods=['POST'])
def create_user():

    user["profileType"] = "INDIVIDUAL"
    user["clientUserId"] = str(uuid.uuid4())
    user["firstName"] = request.form["firstName"]
    user["lastName"] = request.form["lastName"]
    user["email"] = request.form["email"]
    user["dateOfBirth"] = request.form["dateOfBirth"]
    user["addressLine1"] = request.form["addressLine1"]
    user["city"] = request.form["city"]
    user["country"] = request.form["country"]
    user["stateProvince"] = request.form["stateProvince"]
    user["postalCode"] = request.form["postalCode"]

    response = api.createUser(user)

    user["token"] = response.json()["token"]

    return redirect(url_for('add_bank'))

app.run(debug=True)
