from flask import Flask,request
from datetime import date

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'hello world'

# users
@app.route('/users', methods=['GET'])
def users():
  users = [
    {
      'name': "Oma",
      'age': 24,
      'gender': 'female',
      'rentals': 0,
      'date joined': date.today().strftime('%B %d, %Y')
    },
    {
      'name': "Tunde",
      'age': 33,
      'gender': 'male',
      'rentals': 0,
      'date joined': date.today().strftime('%B %d, %Y')
    }
  ]
  return {"users": users}

# @app.route('/profile/<id>', methods=['GET'])
# def get_user(id):

if __name__ == '__main__':
  app.run(debug=True)