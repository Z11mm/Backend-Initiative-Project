from flask import Flask,request,render_template,jsonify
import json
from users_db import users
from movies_db import movies
from rentals_db import rentals

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('index.html')

# USERS
# get all users
@app.route('/users', methods=['GET'])
def get_users():
  return jsonify(users)

# signup user
@app.route('/signup', methods=['GET','POST'])
def add_user():
  if request.method == 'POST':
    new_user = request.get_json()
    users.append(new_user)
    return new_user
  else:
    return render_template('signup.html')
  
# login user
@app.route('/login', methods=['POST'])
def login_user():
  user_credentials = request.get_json()

  for user in users:
    if (users[2]["email"] == user_credentials["email"] and users[2]["password"] == user_credentials["password"]):
      return render_template('success.html')
    else:
      return render_template('index.html')

# get a user
@app.route('/profile/<int:id>', methods=['GET'])
def get_user(id):
  for client in users_db["users"]:
    if (users_db["users"][0]["id"] == id):
      return users_db["users"][0]
    else:
      return render_template('index.html')

# MOVIES
# get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
  return jsonify(movies)

# add a movie

# rentals
# get all rentals
@app.route('/rentals', methods=['GET'])
def get_rentals():
  return jsonify(rentals)

if __name__ == '__main__':
  app.run(debug=True)