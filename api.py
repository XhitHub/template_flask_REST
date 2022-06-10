from flask import Flask
from flask_restful import Resource, Api
#CAS login
from flask_cas import CAS, login_required, login, logout

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)