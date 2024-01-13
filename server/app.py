#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Newsletter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Index(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome to the Newsletter RESTful API",
        }

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response

api.add_resource(Index, '/')

def post(self):

    new_record = Newsletter(
        title=request.form['title'],
        body=request.form['body'],
    )

    db.session.add(new_record)
    db.session.commit()

    response_dict = new_record.to_dict()

    response = make_response(
        jsonify(response_dict),
        201,
    )

    return response