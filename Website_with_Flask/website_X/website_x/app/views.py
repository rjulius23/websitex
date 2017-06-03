from flask import redirect, url_for, request, render_template, flash
from app import app
import sqlite3 as sql

@app.route('/')
@app.route('/index')
def index():
        if request.args:
            logged_in = request.args['logged_in']
            user = request.args['user']
            if logged_in:
                return render_template('index.html', user=user, logged_in=True)
        else:
            return render_template('index.html')

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
            #flash('Login failed!')
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index', user=user, logged_in=True))
    else:
        flash('Login failed!')
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