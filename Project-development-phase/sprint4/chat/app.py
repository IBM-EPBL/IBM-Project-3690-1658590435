from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

import ibm_db

conn = ibm_db.connect(
    "DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xkm46449;PWD=agj8QpL2r0Mp1y33",
    '', '')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('loginpage.html')


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

@app.route('/addre', methods=['POST', 'GET'])
def addre():
    if request.method == 'POST':


        email = request.form['emailid']
        password = request.form['password']

        sql = "SELECT * FROM registration WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('index.html')
        else:
            return render_template('registration.html')

@app.route('/finance')
def finance():
    return render_template('Financialaccount.html')
@app.route('/addFinanceAccount', methods=['POST', 'GET'])
def addFinanceAccount():
    if request.method == 'POST':

        user_id = request.form['add_account_user_id']
        holders_name = request.form['add_account_holders_name']
        account_no = request.form['add_account_acc_num']
        # acc_id user_id holders_name account_no is_active

        sql = "SELECT * FROM financial_account order by id desc"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.execute(stmt)
        financial_account = ibm_db.fetch_assoc(stmt)
        id = 1
        while financial_account != False:
            id1 = financial_account.get("id")
            financial_account = ibm_db.fetch_assoc(stmt)
        id1 = id + 1


        insert_sql = "INSERT INTO financial_account VALUES (?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, id1)
        ibm_db.bind_param(prep_stmt, 2, user_id)
        ibm_db.bind_param(prep_stmt, 3, holders_name)
        ibm_db.bind_param(prep_stmt, 4, account_no)

        ibm_db.execute(prep_stmt)

        print("Financial Account Data saved successfuly..")
        # return render_template('manageExpenses.html')
        return render_template('index.html')


@app.route('/expense')
def expense():
    return render_template('addexpense.html')

@app.route('/addExpense', methods=['POST', 'GET'])
def addExpense():
    if request.method == 'POST':
        user_id = request.form['add_expense_user_id']
        acc_id = request.form['add_expense_acc_id']
        exp_type = request.form['add_expense_type']
        sub_type = request.form['add_expense_sub_type']
        amount = request.form['add_expense_amount']
        date = request.form['add_expense_date']


        # acc_id user_id holders_name account_no is_active

        sql = "SELECT * FROM expenses order by exp_id desc limit 1"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.execute(stmt)
        expenses = ibm_db.fetch_assoc(stmt)

        id = 0
        while expenses != False:
            id = expenses.get("exp_id")
            expenses = ibm_db.fetch_assoc(stmt)
        id = id + 1

        insert_sql = "INSERT INTO expenses VALUES (?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, id)
        ibm_db.bind_param(prep_stmt, 2, user_id)
        ibm_db.bind_param(prep_stmt, 3, acc_id)
        ibm_db.bind_param(prep_stmt, 4, exp_type)
        ibm_db.bind_param(prep_stmt, 5, sub_type)
        ibm_db.bind_param(prep_stmt, 6, amount)
        ibm_db.bind_param(prep_stmt, 7, date)



        ibm_db.execute(prep_stmt)

        print("Expenses  Data saved successfuly..")
        # return render_template('manageExpenses.html')
        return render_template('index.html')
@app.route("/result")
def result():
    expenses = []
    sql = "SELECT * FROM expenses"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        # print ("The Name is : ",  dictionary)
        expenses.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if expenses:
        return render_template("result.html",expenses=expenses)


@app.route('/analysis', methods=['POST', 'GET'])
def analysis():
    if request.method == 'POST':
        userid = request.form['userid']
        salary = request.form['sal']
    return render_template('res.html',msg="you have enough money to spend")










