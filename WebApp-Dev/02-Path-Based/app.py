from flask import Flask
import os 
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/amit")
def hello_amit():
    return "Hello EveryOne from Amit Vashist"


if __name__ == "__main__":
   app.run()
