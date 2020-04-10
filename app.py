import os
from flask import Flask, render_template, flash, redirect, render_template, request, session, abort,send_from_directory,url_for


#from werkzeug.utils import secure_filename
#from OpenSSL import SSL
#import ldap

app = Flask(__name__)

  	

@app.route('/')
def test():
    return render_template('index.html')

    
@app.route('/auth', methods=['POST'])
def check_hostname():
    email =    request.form['username']
    password = request.form['pass']
    if email=="khalid" and password=="C0ron@":
        return "You have successfully authenticated"
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=3030)
