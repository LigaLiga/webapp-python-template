from flask import Flask, Response
import json

from Applicaton import applications


app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/jquery-3.4.1.min.js')
def js():
    return app.send_static_file('jquery-3.4.1.min.js')

@app.route("/data")
def data():
    json_string = json.dumps([applicaton.__dict__ for application in applications])
    return Response(json_string, mimetype='application/json')