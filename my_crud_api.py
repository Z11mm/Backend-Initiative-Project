from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

# users
@app.route('/users')
def users():
  return 'Welcome back'

# movies
@app.route('/movies')
def movies():
  return 'Categories'

# rentals
@app.route('/rentals')
def rentals():
  return 'Rent a movie'

if __name__ == '__main__':
  app.run()