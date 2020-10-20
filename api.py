import flask
from flask import request, jsonify
import requests
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return 'An api that tells you whether or not a home has a septic tank'

@app.route('/api', methods=['GET','POST'])
def api():
    endpoint = "http://127.0.0.1:5001/canaryapi"
    response = requests.post(endpoint, auth = ('apikey', 'apisecret'), params = {'address': request.args.get('address'), 'zipcode':request.args.get('zipcode')})
    if (response.status_code == 200):
        homedata = json.loads(response.text)
        if (homedata["sewer"] == 'septic'):
          return jsonify({"septic":"true"})
        else:
          return jsonify({"septic":"false"})
    else:
        return "Invalid response from Canary API"

app.run(host='127.0.0.1',port=5000)
