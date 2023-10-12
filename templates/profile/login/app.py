from flask import Flask, render_template, request, redirect, url_for
import os
path=os.getcwd()
app = Flask(__name__,template_folder=path)

# Dummy user data (replace this with a database in a real application)
users = {
    "1": "1"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Login successful, redirect to a success page
        return render_template(R'C:\Users\philo\Documents\GitHub\Project-X\profile\index.html')
    else:
        # Login failed, redirect back to the login page
        message='Invalid Username or Password'
        return redirect(url_for('index.html',message=message))

@app.route('/success/<username>')
def success(username):
    return f'Welcome, {username}! Login successful.'

if __name__ == '__main__':
    app.run(debug=True)
