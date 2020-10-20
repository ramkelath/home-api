import flask
from flask import request, jsonify, abort
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 'An api that mimics, very minimally, the canary home api'

@app.route('/canaryapi', methods=['GET','POST'])
def canary():
    auth = request.authorization
    if (auth.username != 'apikey' or auth.password != 'apisecret'):
        abort(403)
    zip = int(request.args.get('zipcode'))
    if (zip % 6 == 0):
      return jsonify({"sewer":"septic"})
    else:
      return jsonify({"sewer":"municipal"})

app.run(host='127.0.0.1',port=5001)
