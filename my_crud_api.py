from flask import Flask, request
import json
from users_db import users_db
from movies_db import movies_db
from rentals_db import rentals_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'hello world'

# users
@app.route('/users', methods=['GET'])
def get_users():
  users = json.dumps(users_db)
  return users

# @app.route('/profile/<id>', methods=['GET'])
# def get_user(id):

# movies
@app.route('/movies', methods=['GET'])
def get_movies():
  movies = json.dumps(movies_db)
  return movies

# rentals
@app.route('/rentals', methods=['GET'])
def get_rentals():
  rentals = json.dumps(rentals_db)
  return rentals

if __name__ == '__main__':
  app.run(debug=True)