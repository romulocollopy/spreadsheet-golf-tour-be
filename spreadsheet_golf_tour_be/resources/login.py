from flask_restful import Resource


class LoginResource(Resource):
    def get(self):
        return "Login Here"
