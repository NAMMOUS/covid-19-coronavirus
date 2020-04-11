import os
from flask import Flask, render_template, flash, redirect, render_template, request, session, abort,send_from_directory,url_for
import requests
import json



app = Flask(__name__)

def corona(code):
    url = "https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code="+code
    response = requests.request("GET", url)
    my_json=json.loads(response.text)
    return str(my_json['latest']['confirmed'])

def data(code,value):
    ch='{"country":'+'"'+code+'",'
    ch= ch +'"cases":"'+value+'"}'
    my_json=json.loads(ch)
    return my_json


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        liste=[]
        codes=["MA","FR","IT","DE","ES","DZ","TR","US","CN","CA","EG","IN","IR","IL","JP","LY"]
        countries=["MAROC","FRANCE","ITALIE","ALLEMAGNE","ESPAGNE","ALGERIE","TURQUIE","ETATS-UNIES","CHINE","CANADA","EGYPTE","INDE","IRAN","ISRAEL","JAPON","LIBYE"]
        for i,j in zip(countries,codes):
            liste.append(data(i,corona(j)))
        return render_template('index.html',ma=liste)
        

    
@app.route('/login', methods=['POST'])
def check_credential():
    email =    request.form['username']
    password = request.form['pass']
    if email=="khalid" and password=="C0ron@":
        session['logged_in']=True
    else:
        flash('wrong password!')
    return home()
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=3030)
