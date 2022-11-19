from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

import ibm_db

conn = ibm_db.connect(
    "DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xkm46449;PWD=agj8QpL2r0Mp1y33",
    '', '')

app = Flask(__name__)
@app.route('/add')
def new_student():
    return render_template('registration.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM registration WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('loginpage.html', msg="You are already a member, please login using your details")
        else:
            insert_sql = "INSERT INTO registration VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)

            ibm_db.execute(prep_stmt)

        return render_template('loginpage.html', msg=" Data saved successfuly..")
