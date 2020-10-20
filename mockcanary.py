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
      sewertype = "septic"
    else:
      sewertype = "other"
    mock_json = '{ "property/details": { "api_code_description": "ok", "api_code": 0, "result": { "property": { "air_conditioning": "yes", "attic": false, "basement": "full_basement", "building_area_sq_ft": 1824, "building_condition_score": 5, "building_quality_score": 3, "construction_type": "Wood", "exterior_walls": "wood_siding", "fireplace": false, "full_bath_count": 2, "garage_parking_of_cars": 1, "garage_type_parking": "underground_basement", "heating": "forced_air_unit", "heating_fuel_type": "gas", "no_of_buildings": 1, "no_of_stories": 2, "number_of_bedrooms": 4, "number_of_units": 1, "partial_bath_count": 1, "pool": true, "property_type": "Single Family Residential", "roof_cover": "Asphalt", "roof_type": "Wood truss", "site_area_acres": 0.119, "style": "colonial", "total_bath_count": 2.5, "total_number_of_rooms": 7, "sewer": "' + sewertype + '", "subdivision" : "CITY LAND ASSOCIATION", "water": "municipal", "year_built": 1957, "zoning": "RH1" }, "assessment":{ "apn": "0000 -1111", "assessment_year": 2015, "tax_year": 2015, "total_assessed_value": 1300000.0, "tax_amount": 15199.86 } } } }'
    return mock_json

app.run(host='127.0.0.1',port=5001)
