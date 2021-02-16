#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def root_index():
    greeting = "New greeting"
    variable = "Homepage"
    return render_template("index.html", greeting=greeting, variable=variable)

@app.route("/create_account", methods = ['POST', 'GET'])
def account_index():
    if request.method == "POST":
        email = request.form['email']
        username = request.form['user']
        password = request.form['pass']
        output = "Please enter a valid email"
        return render_template("create_account.html", output=output)
    else:
        return render_template("create_account.html")

@app.route("/login", methods = ['POST', 'GET'])
def login_index():
    if request.method == "POST":
        username = request.form['user']
        password = request.form['pass']
        output = "Incorrect password"
        return render_template("login_form.html", output=output)
    else:
        return render_template("login_form.html")

@app.route("/shop")
def shop_index():
    return render_template("shop.html")

@app.route("/cart")
def cart_index():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run()


