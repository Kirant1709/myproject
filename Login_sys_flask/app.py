from flask import Flask,request,render_template, redirect
import os
import sqlite3


# current directory 
mypath = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

#defining homepage
@app.route('/')
def homepage():
    return render_template("home.html")

#function for login authentication 
@app.route('/',methods=["POST"])
def login():
    uname = request.form['Username']
    email = request.form['Email']
    passwrd = request.form['Password']
    
    connection = sqlite3.connect(mypath + "\mylogin.db")
    cursor = connection.cursor()
    query1 = "SELECT Email, Password from Users WHERE Email = '{em}' AND Password = '{pw}'".format(em = email, pw=passwrd)
    
    rows = cursor.execute(query1)
    rows = rows.fetchall()

    if len(rows) == 1:
        return render_template("loggedin.html")
    else:
        return render_template("invalid_credentials.html")    

#function for registering user
@app.route('/register', methods=['GET','POST'])
def registerpage():
    if request.method == "POST":
        duname = request.form['Dusername']
        dPasswrd = request.form['Dpassword']
        Uemail = request.form['Emailuser']
        connection = sqlite3.connect(mypath + "\mylogin.db")
        cursor = connection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}', '{e}', '{p}')".format(u=duname, e=Uemail, p=dPasswrd)
        cursor.execute(query1)
        connection.commit()
        return redirect("/")
    return render_template("Register.html")    
      
if __name__ == '__main__':
    app.run()















