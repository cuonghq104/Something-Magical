from flask import Flask
import mlab
from mongoengine import *
from flask_restful import Resource, Api, reqparse
import json

mlab.connect()


class Celebrity(Document):
    name = StringField()
    proper_name = StringField()
    birthday = StringField()
    birthplace = StringField()
    nationality = StringField()
    occupation = StringField()
    height = IntField()
    about = StringField()
    before_fame = StringField()
    trivia = StringField()
    family_life = StringField()
    associated_with = StringField()
    websites = ListField(StringField())
    images = ListField(StringField())
    married = BooleanField()

# n = Celebrity(name="tao",nationality="que tao")
# n.save()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, location="json")
parser.add_argument("proper_name", type=str, location = "json")
parser.add_argument("birthday", type=str, location = "json")
parser.add_argument("birthplace", type=str, location = "json")
parser.add_argument("nationality", type=str, location="json")
parser.add_argument("occupation", type=str, location = "json")
parser.add_argument("height", type=int, location = "json")
parser.add_argument("about", type=str, location = "json")
parser.add_argument("before_fame", type=str, location = "json")
parser.add_argument("trivia", type=str, location = "json")
parser.add_argument("family_life", type=str, location = "json")
parser.add_argument("associated_with", type=str, location = "json")
parser.add_argument("websites", type=list, location = "json")
parser.add_argument("images", type=list, location = "json")
parser.add_argument("married", type=bool, location = "json")

# for celeb in Celebrity.objects:
#     print(celeb.to_json())
#

@app.route('/')
def hello_world():
    return 'Hello World!'


class CelebrityListRes(Resource):

    def get(self):
        return mlab.list2json(Celebrity.objects)

    def post(self):
        args = parser.parse_args()
        name = args["name"]
        proper_name = args["proper_name"]
        birthday = args["birthday"]
        birthplace = args["birthplace"]
        nationality = args["nationality"]
        occupation = args["occupation"]
        height = args["height"]
        about = args["about"]
        before_fame = args["before_fame"]
        trivia = args["trivia"]
        family_life = args["family_life"]
        associated_with = args["associated_with"]
        websites = args["websites"]
        images = args["images"]
        married = args["married"]

        new_celeb = Celebrity()
        new_celeb.name=name
        new_celeb.nationality=nationality
        new_celeb.nationality=nationality
        new_celeb.proper_name=proper_name
        new_celeb.birthday=birthday
        new_celeb.birthplace=birthplace
        new_celeb.nationality=nationality
        new_celeb.occupation=occupation
        new_celeb.height=height
        new_celeb.about=about
        new_celeb.before_fame=before_fame
        new_celeb.trivia=trivia
        new_celeb.family_life=family_life
        new_celeb.associated_with=associated_with
        new_celeb.websites=websites
        new_celeb.images=images
        new_celeb.married=married

        new_celeb.save()
        return mlab.item2json(new_celeb)

class CelebrityRes(Resource):

    def get(self, celebrity_id):
        all_celebs = Celebrity.objects
        found_celeb = all_celebs.with_id(celebrity_id)
        return mlab.item2json(found_celeb)

    def delete(self, celebrity_id):
        all_celebs = Celebrity.objects
        found_celeb = all_celebs.with_id(celebrity_id)
        found_celeb.delete()
        return {"status": "Ok", "code": 1}, 200

    def put(self, celebrity_id):
        #parse args
        args = parser.parse_args()
        name = args["name"]
        proper_name = args["proper_name"]
        birthday = args["birthday"]
        birthplace = args["birthplace"]
        nationality = args["nationality"]
        occupation = args["occupation"]
        height = args["height"]
        about = args["about"]
        before_fame = args["before_fame"]
        trivia = args["trivia"]
        family_life = args["family_life"]
        associated_with = args["associated_with"]
        websites = args["websites"]
        images = args["images"]
        married = args["married"]
        #find note
        all_celebs = Celebrity.objects
        found_celeb = all_celebs.with_id(celebrity_id)
        #
        found_celeb.update(set__name=name, set__nationality=nationality,set__proper_name=proper_name, set__birthday=birthday, set__birthplace=birthplace, set__occupation=occupation, set__height=height, set__about=about, set__family_life=family_life, set__before_fame=before_fame, set__trivia=trivia, set__associated_with=associated_with, set__images=images, set__websites=websites, set__married=married)
        return {"status": "Ok", "code": 1}, 200


api.add_resource(CelebrityListRes, "/api/celebrity")
api.add_resource(CelebrityRes, "/api/celebrity/<celebrity_id>")

if __name__ == '__main__':
    app.run()
