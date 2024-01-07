
from db import *
from catalogue import *
from datetime import *
import time
import sys
import mysql.connector

# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from register import app as reg_app
app = Flask(__name__)
app.debug = True
cnx = mysql.connector.connect(user='myflix-user-db', password='password',host='34.89.18.21')
cursor = cnx.cursor()
create_database(cnx,cursor)


@app.route('/Sub')
def sub_page():
    return 'Sub Page'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']

       
        login = find_user(username,password)
        if login == 1:
             return redirect('/cat_page')
        else:
             return redirect('/register')
    return render_template('login.html', error=error)



def find_user(username, keynum):
    cnx = mysql.connector.connect(user='myflix-user-db', password='password',host='34.89.18.21')
    cursor = cnx.cursor()


    query = "SELECT username,keynum FROM AccessKeys.AccessKey WHERE username = %s AND keynum = %s"
    cursor.execute(query, (username, keynum))
    result = cursor.fetchone()

    if result is not None:

        return 1
    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="80")
