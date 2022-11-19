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
