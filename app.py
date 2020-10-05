from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)      # 상속

class Rest(Resource):
    def get(self):
        return {'rest':'Good'}

api.add_resource(Rest, '/')

# @app.route('/')
# def idx():
#     return {'rest' : 'OK'}

# @app.route('/rest')
# def idx():
#     return {}

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)