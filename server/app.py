class NewsletterByID(Resource):

    def get(self, id):

        response_dict = Newsletter.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )

        return response

api.add_resource(NewsletterByID, '/newsletters/<int:id>')

Only two differences between this and our original GET route:

We need to include id in our method's arguments and the resource URL.
We need to chain some commands together to get the record with the provided id.
Check out this lesson's finished product: open Postman and navigate to http://127.0.0.1:5555/newsletters/20Links to an external site.. Make sure that your request method is GET, then click submit. You should see something similar to the following:

{
    "body": "College tax head change. Claim exactly because choose. Church edge center across test stock.",
    "edited_at": null,
    "id": 20,
    "published_at": "2022-09-21 18:35:17",
    "title": "Court probably not."
}
Conclusion
Flask-RESTful is a very simple tool that allows us to properly and effectively use HTTP request methods in our applications. Like other extensions, it reduces the amount of code you have to write to accomplish common tasks- and if you don't need to accomplish those common tasks, you can just leave it out!

Solution Code
#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Newsletter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

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
            200,
        )

        return response

api.add_resource(Index, '/')

class Newsletters(Resource):

    def get(self):

        response_dict_list = [n.to_dict() for n in Newsletter.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response

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

api.add_resource(Newsletters, '/newsletters')

class NewsletterByID(Resource):

    def get(self, id):

        response_dict = Newsletter.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )

        return response

api.add_resource(NewsletterByID, '/newsletters/<int:id>')


if __name__ == '__main__':
    app.run(port=5555)
