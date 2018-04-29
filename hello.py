from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'message': "hello, world!"})

@app.route("/login")
def login():
    return "please log in"