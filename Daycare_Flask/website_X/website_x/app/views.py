from flask import redirect, url_for, request, render_template
from app import app
import sqlite3 as sql

@app.route('/')
@app.route('/index')
def index():
        return redirect(url_for("login"))

@app.route('/login')
def login():
    return render_template('login_v1.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success', methods = ['POST','GET'])
def success():
    if request.method == 'POST':
        user = request.form['userID']
        passwd = request.form['password']
        typeUser = request.form['userType']

        with sql.connect("users.db") as con:
            cur = con.cursor()
            cur.execute("SELECT name,password,type FROM users WHERE name=? AND password=? AND type=?",(user,passwd,typeUser) )
            res = cur.fetchall()
            print (res)
        if len(res) == 0:
            return redirect(url_for('register'))
        else:
            return "Successful login[%s] for user:%s with password:%s" % (typeUser,user,passwd)
    else:
        return "LOGIN FAILED!!"


@app.route('/registered', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user = request.form['userID']
        passwd = request.form['password']
        typeUser = request.form['userType']

        with sql.connect("users.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (name,password,type)VALUES(?, ?, ?)", (user, passwd, typeUser))
            con.commit()
            msg = "Record successfully added"

        return "Successful registration  for user:%s [%s] with password:%s" % (user, typeUser, passwd)
    else:
        return redirect(url_for('login'))