from flask import Flask
# from flask_restful import Api, Resource

app = Flask(__name__)
# api = Api(app)

# class User(Resource):
#   def get(self, user_id):
#     return {user_id: users[user_id]}

#   def post(self, user_id):
#     users[user_id] = request.form['data']
#     return {user_id: users[user_id]},201

# api.add_resource(User, '/users/<string:user_id>')

# @app.route('/')
# def hello_world():
#   return 'hello world'

# users
# @app.route('/users')
# def users():
#   return 'Welcome back'

# movies
# @app.route('/movies')
# def movies():
#   return 'Categories'

# rentals
# @app.route('/rentals')
# def rentals():
#   return 'Rent a movie'

if __name__ == '__main__':
  app.run(debug=True)