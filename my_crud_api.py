from flask import Flask, request, render_template
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
@app.route('/signup', methods=['POST'])
def add_user():
  new_user = request.get_json()   
  return new_user
  
# login user
@app.route('/login', methods=['POST'])
def login_user():
  user_credentials = request.get_json()
  return user_credentials

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