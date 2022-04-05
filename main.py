import flask
from flask import Flask,render_template,request
import sqlite3

con=sqlite3.connect("studentmanagement.db",check_same_thread=False)
listOfTables=con.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENTS' ").fetchall()

if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    con.execute(''' CREATE TABLE STUDENTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,BRANCH TEXT,SEMESTER INTEGER,
    ROLLNUMBER INTEGER,
    ADMNO INTEGER,PASSWORD TEXT,DOB TEXT
    ); ''')
    print("Table has created")

app=Flask(__name__)

@app.route("/")
def studlogin():
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        getName=request.form["Name"]
        getAdno=request.form["Admission no"]
        getBranch=request.form["Branch"]
        getRoll = request.form["Roll no"]
        getbday = request.form["Birth date"]
        getsemester = request.form["semester"]
        getpassword = request.form["password"]
        getcpassword = request.form["confirm password"]

        print(getName)
        print(getAdno)
        print(getBranch)
        print(getRoll)
        print(getbday)
        print(getsemester)
        print(getpassword)
        print(getcpassword)
        try:
            con.execute("INSERT INTO STUDENTS(NAME,BRANCH,SEMESTER,ROLLNUMBER,ADMNO,PASSWORD,DOB) VALUES('"+getName+"','"+getBranch+"',"+getsemester+","+getRoll+","+getAdno+",'"+getpassword+"',"+getbday+")")
            print("Successfully Inserted")

        except Exception as e:
            print(e)

    return render_template("register.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()