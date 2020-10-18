# home-api
REST API whose response tells you whether or not a residence has a septic sewer system.

This API returns a JSON string with a single key 'septic' and a boolean value - true or false.  

Running the API:

1. Prerequisites:

Python/Pip/Flask

Verify that you have Python and pip installed on your system (at command line: python --version; pip --version). Install if needed.
See if flask is installed on your system: flask --version. If not, install: pip install flask.

2. Clone this repository. Go to a suitable user folder in your file system and run the following command: 


3. Run the api: python api.py.  Note the port number that is serving the api (e.g. * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit))

4. Send a request to the api using your browser (or command line or an application) :  http://127.0.0.1:5000/?address=123+Main+St&zipcode=94132
