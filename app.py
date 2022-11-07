
from db import *

from flask import*



app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/pack")
def pacakes():
    return render_template("packages.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/log")
def log():
    return render_template("login.html")

@app.route("/wel")
def welcome():
    return render_template("welcome.html")

@app.route("/begi")
def beginners():
    return render_template("beg.html")

@app.route("/push")
def pp():
    return render_template("pushpull.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/detail")
def detail():
    return render_template("details.html")
   
@app.route("/insert_data",methods=["post"])
def ins():
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    age=request.form["age"]
    Weight=request.form["Weight"]
    Membership_Months=request.form["months"]
    Choose_password=request.form["password"]
    t=(name,phone,email,age,Weight,Membership_Months,Choose_password)
    insert(t)
    return redirect("/")

@app.route("/show_data1", methods=["post"])
def showadmin():
    email=request.form["email"]
    passw=request.form["password"]
    if email=="kunalpatilkd@gmail.com" and  passw=="12345":
         return render_template("showdetails.html")
    else:
        
        return render_template("home.html")
    
    
    
@app.route("/show_data", methods=["post"])
def shw():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=check(email)
    if t in t1:
         return render_template("Welcome.html")
    else:
        
        return render_template("home.html")
    
    
   
    







if __name__ == "__main__":
    app.run(debug=True)