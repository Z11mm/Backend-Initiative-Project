from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/users')
def users():
  return 'Welcome back'

@app.route('/movies')
def movies():
  return 'Categories'

@app.route('/rentals')
def rentals():
  return 'Rent a movie'

if __name__ == '__main__':
  app.run()