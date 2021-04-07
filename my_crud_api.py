from flask import Flask,request,render_template
import json
from users_db import users_db
from movies_db import movies_db
from rentals_db import rentals_db

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('index.html')

# USERS
# get all users
@app.route('/users', methods=['GET'])
def get_users():
  users = json.dumps(users_db)
  return users

# signup user
@app.route('/signup', methods=['GET','POST'])
def add_user():
  users = json.dumps(users_db)
  if request.method == 'POST':
    new_user = request.get_json()
    users_db["users"].append(new_user)
    return new_user
  else:
    return render_template('signup.html')
  
# login user
@app.route('/login', methods=['POST'])
def login_user():
  user_credentials = request.get_json()
  
  for client in users_db["users"]:
    if (users_db["users"][0]["email"] == user_credentials["email"] and users_db["users"][0]["password"] == user_credentials["password"]):
      return render_template('success.html')
    else:
      return render_template('index.html')

# movies
# get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
  movies = json.dumps(movies_db)
  return movies

# rentals
# get all rentals
@app.route('/rentals', methods=['GET'])
def get_rentals():
  rentals = json.dumps(rentals_db)
  return rentals

if __name__ == '__main__':
  app.run(debug=True)