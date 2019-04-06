from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

movies = []
m1 = {'title': 'Lord of The Rings',
      'category': 'Fantasy',
      'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
      }
movies.append(m1)


@api.resource('/movie')
class Movie(Resource):
    def get(self):
        return movies


if __name__ == '__main__':
    app.run(debug=True)
