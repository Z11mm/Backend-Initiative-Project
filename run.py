# Run app on flask server
from src import create_app

myapp = create_app()

if __name__ == '__main__':
  myapp.run(debug=True)