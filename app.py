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

    if username in users and users[username] == password:
        # Successful login, redirect to a different page
        return redirect(url_for("profile",username=username))
    else:
        # Invalid credentials, show an error message
        error = "Invalid username or password. Please try again."
        return render_template("login/index.html", error=error)


@app.route("/profile/<username>")
def profile(username):
    j=0
    for i in range(len(users_list)):
        if users_list[i][0]==username:
            j=i
            pass
    name=users_list[i][0]
    yr=users_list[i][1]
    sem=users_list[i][2]
    dep=users_list[i][3]
    regno=users_list[i][4]
    roll=users_list[i][5]
    email=users_list[i][6]
    phone=users_list[i][7]
    username=users_list[j]
    return render_template("profile/index.html",username=username)
    


@app.route("/welcome")
def welcome():
    return "Welcome to the protected area!"


if __name__ == "__main__":
    app.run(debug=True)
