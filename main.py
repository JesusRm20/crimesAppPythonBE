from flask import Flask, jsonify, json, redirect, url_for, render_template, request, flash, session
import requests
import userClasses
import passwordHash
import task
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "Jesus"

@app.route('/signup', methods=['POST'])
def signup():
    usr = json.loads((request.data.decode('utf-8')))
    resp = userClasses.addUser(usr)
    if resp:
        return 'User added Successfully.'
    return 'Something went Wrong.'

@app.route('/load', methods=['GET','POST'])
def loadCrimes():
        date = json.loads((request.data.decode('utf-8')))
        res = task.selectCrimeByDate(date['date'])
        if res > 0:
             return 'false'
        else:
            crimeDetails = task.loadStreetLevelCrimes(date['date'])
            return 'true'
       

@app.route('/login', methods=['POST'])
def login():
    usr = json.loads((request.data.decode('utf-8')))
    print(usr['userName'].strip())
    resp = userClasses.getUser(usr['userName'].strip())
    print(resp)
    if resp != '':
        ver = passwordHash.passwordCheck(usr['password'].strip(), resp['password'].strip()) 
        del resp['password']
        if ver:
            return {'val': 'true', 'token': userClasses.genToken(resp).decode('utf-8')}
    return {'val': 'false', 'token': 'null'}    
  

@app.route('/home', methods=['GET', 'POST'])
def home():
    resp = task.getStreestLevelCrimes()
    return jsonify(resp)

@app.route('/updateCrime', methods=['PUT'])
def updateCrime():
    obj = json.loads((request.data.decode('utf-8')))['obj']
    crime = {}
    crime['id'] = obj['id']
    crime['category'] = obj['category']
    crime['location_type'] = obj['location_type']
    crime['latitude'] = obj['latitude']
    crime['longitude'] = obj['longitude']
    crime['street_name'] = obj['street_name']
    crime['month'] = obj['month']
    update = task.updateCrime(crime)
    if update:
        crimeDetails = task.getStreestLevelCrimesId(obj['id'])
        persistent_id = crimeDetails[0].persistent_id
        crimeOutcomes = task.getCrimesOutcome(persistent_id)

    crime = task.formatCrimeOutcomes(crimeDetails, crimeOutcomes)
    return crime
    
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    update = task.deleteOutcome(id)
    if update:
        return 'true'
    else:
        'false'

@app.route('/edit/<id>', methods=['GET','POST'])
def editCrime(id):
    crimeDetails = task.getStreestLevelCrimesId(id)
    persistent_id = crimeDetails[0].persistent_id
    count = task.countCrimesOutcome(persistent_id)
    if count > 0:
        crimeOutcomes = task.getCrimesOutcome(persistent_id.strip())
    else:
        task.loadCrimesOutcome(persistent_id.strip())
        crimeOutcomes = task.getCrimesOutcome(persistent_id.strip())
    crime = task.formatCrimeOutcomes(crimeDetails, crimeOutcomes)

    return crime 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)