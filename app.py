from flask import Flask, render_template, request, redirect, url_for
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["studentusercred"]
# Dummy user data for demonstration (replace this with a database in a real application)
users = {"valan": "priyanka",
         "neelam" :"merlyn",
         "sairam" : "Lancey"}
users_list=[["valan","II","3","CSE","311122104125","22cs199","Valan@gmail.com","83572527357",],
            ["neelam","II","3","CSE","311122104125","22cs199","neelam@gmail.com","83572527357",],
            ["sairam","II","3","CSE","311122104125","22cs199","lancey@gmail.com","83572527357",],
            ["philo","II","3","CSE","311122104125","22cs199","philo@gmail.com","83572527357",],
            ["admin","II","3","CSE","311122104125","22cs199","admin@gmail.com","83572527357",]]

@app.route("/")
def index():
    return render_template("login/index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    result = collection.find_one({"key": "value"})
    query={"Roll No":username}
    resultt=collection.find_one(query)
    result=str(resultt["Reg No"])
    if password==result:
        print("done")
        return redirect(url_for("profile",username=username))
    else:
        # Invalid credentials, show an error message
        error = "Invalid username or password. Please try again."
        return render_template("login/index.html", error=error)


@app.route("/profile/<username>")
def profile(username):
    query={"Roll No":username}
    resultt=collection.find_one(query)
    print(resultt)
    name=resultt["name"]
    print(name)
    roll=resultt["Roll No"]
    reg=resultt["Reg No"]
    yr=resultt["Yr"]
    age=resultt["Age"]
    sem=resultt["Sem"]
    dob=resultt["DOB"]
    email=resultt["Email"]
    cls=resultt["Cls"]
    ph=resultt["phone"]
    return render_template("profile/index.html",username=username,result=resultt,name=name,roll=roll,reg=reg,yr=yr,age=age,sem=sem,dob=dob,email=email,cls=cls,ph=ph)
    


@app.route("/welcome")
def welcome():
    return "Welcome to the protected area!"


if __name__ == "__main__":
    app.run(debug=True)
