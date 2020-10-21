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
    # The following two values should ideally be read from an encrypted file in the filesystem
    username = 'apikey'
    password = 'apisecret'
    endpoint = "http://127.0.0.1:5001/canaryapi"  # In the real world this would go to https://api.housecanary.com/v2/property/details
    try:
        response = requests.post(endpoint, auth = (username, password), params = {'address': request.args.get('address'), 'zipcode':request.args.get('zipcode')})
        if (response.status_code == 200):
            homedata = json.loads(response.text)
            if (homedata["property/details"]["result"]["property"]["sewer"] == 'septic'):
              return jsonify({"septic":"true"})
            else:
              return jsonify({"septic":"false"})
        else:
            return "Invalid response from Canary API"
    except:
        return "Could not connect to Canary API"

app.run(host='127.0.0.1',port=5000)
