from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xkm46449;PWD=agj8QpL2r0Mp1y33",'','')

app = Flask(__name__)



@app.route('/')
def home():
  return render_template('loginpage.html')

@app.route('/reg')
def reg():
  return  render_template('registration.html')
