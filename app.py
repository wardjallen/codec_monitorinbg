from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse


app = Flask(__name__)

api = Api(app)

heath_check_post_parser = reqparse.RequestParser()
heath_check_post_parser.add_argument("serialnumber")

@api.route("/codec/heathcheck")
class CodecHealthCheck(Resource):

    @api.expect(heath_check_post_parser)
    def post(self):
        args = heath_check_post_parser.parse_args()
        return "ok" 
    





if __name__ == "__main__":
    app.run(debug=True)