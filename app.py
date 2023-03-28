from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, request, session, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import connect
from flask_session import Session
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_cors import CORS
import datetime
import os


load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
APP_ENV = os.environ.get('APP_ENV')
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')
SALT_ROUNDS = os.environ.get('SALT_ROUNDS')


app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "spark", "host": MONGO_URI}


CORS(app)
Session(app)
JWTManager(app)
bcrypt = Bcrypt(app)
db = MongoEngine(app)


class Likes(db.EmbeddedDocument):
    users = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Likes, self).save(*args, **kwargs)


class Dislikes(db.EmbeddedDocument):
    users = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Dislikes, self).save(*args, **kwargs)


class Preferences(db.EmbeddedDocument):
    interests = db.ListField(db.StringField())
    neighborhood = db.StringField()
    max_distance = db.IntField()
    max_age = db.IntField()
    min_age = db.IntField()
    age_dealbreaker = db.BooleanField()
    ethnicity = db.ListField(db.StringField())
    religion = db.ListField(db.StringField())
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Preferences, self).save(*args, **kwargs)


class Pictures(db.EmbeddedDocument):
    title = db.StringField()
    image = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Pictures, self).save(*args, **kwargs)


class Prompts(db.EmbeddedDocument):
    title = db.StringField()
    description = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Prompts, self).save(*args, **kwargs)


class Virtues(db.EmbeddedDocument):
    work = db.StringField()
    work_visibility = db.BooleanField()
    job_title = db.StringField()
    job_title_visibility = db.BooleanField()
    school = db.ListField(db.StringField())
    school_visibility = db.BooleanField()
    education_level = db.StringField()
    education_level_visibility = db.BooleanField()
    religious_beliefs = db.ListField(db.StringField())
    religious_beliefs_visibility = db.BooleanField()
    hometown = db.StringField()
    hometown_visibility = db.BooleanField()
    politics = db.StringField()
    politics_visibility = db.BooleanField()
    languages = db.ListField(db.StringField())
    languages_visibility = db.BooleanField()
    dating_intentions = db.StringField()
    dating_intentions_visibility = db.BooleanField()
    relationship_type = db.ListField(db.StringField())
    relationship_type_visibility = db.BooleanField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Virtues, self).save(*args, **kwargs)


class Vitals(db.EmbeddedDocument):
    name = db.StringField()
    name_visibility = db.BooleanField()
    gender = db.StringField()
    gender_visibility = db.BooleanField()
    pronouns = db.ListField(db.StringField())
    pronouns_visibility = db.BooleanField()
    sexuality = db.StringField()
    sexuality_visibility = db.BooleanField()
    age = db.StringField()
    age_visibility = db.BooleanField()
    height = db.StringField()
    height_visibility = db.BooleanField()
    location = db.StringField()
    location_visibility = db.BooleanField()
    ethnicty = db.ListField(db.StringField())
    ethnicity_visibility = db.BooleanField()
    children = db.StringField()
    children_visibility = db.BooleanField()
    family_plans = db.StringField()
    family_plans_visibility = db.BooleanField()
    vaccinated = db.StringField()
    vaccinated_visibility = db.BooleanField()
    pets = db.ListField(db.StringField())
    pets_visibility = db.BooleanField()
    zodiac_sign = db.StringField()
    zodiac_sign_visibility = db.BooleanField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Vitals, self).save(*args, **kwargs)


class Vices(db.EmbeddedDocument):
    drinking = db.StringField()
    drinking_visibility = db.BooleanField()
    smoking = db.StringField()
    smoking_visibility = db.BooleanField()
    marijuana = db.StringField()
    marijuana_visibility = db.BooleanField()
    drugs = db.StringField()
    drugs_visibility = db.BooleanField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Vices, self).save(*args, **kwargs)


class User(db.Document):
    email = db.StringField()
    password = db.BinaryField()
    birthdate = db.StringField()
    pause = db.BooleanField()
    subscriber = db.BooleanField()
    likes = db.EmbeddedDocumentListField(Likes)
    dislikes = db.EmbeddedDocumentListField(Dislikes)
    preferences = db.EmbeddedDocumentField(Preferences)
    pictures = db.EmbeddedDocumentListField(Pictures)
    prompts = db.EmbeddedDocumentListField(Prompts)
    virtues = db.EmbeddedDocumentField(Virtues)
    vitals = db.EmbeddedDocumentField(Vitals)
    vices = db.EmbeddedDocumentField(Vices)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)


def index():
    if not session.get("email"):
        return False
    return True


@app.route("/signup", methods=['POST'])
def signup():
    user = User()
    body = request.get_json()
    email = User.objects(email=body.get("email")).first()
    if email:
        return {"message": "Email already exists"}, 500
    hashed = bcrypt.generate_password_hash(body.get("password"), int(SALT_ROUNDS))
    user.email = body.get("email")
    user.password = hashed
    user.save()
    return {"message": "User created"}, 200


@app.route('/signin', methods=['POST'])
def signin():
    body = request.get_json()
    user = User.objects(email=body.get("email")).first()
    if user:
        if bcrypt.check_password_hash(user["password"], body.get("password")):
            session['email'] = body.get('email')
            access_token = create_access_token(identity=body.get("email"))
            return jsonify(access_token=access_token, user=user, message="User logged in"), 200
        return {"message": "Email & Password combination is wrong"}, 500
    return {"message": "User does not exist"}, 500


@app.route('/logout')
def logout():
    session.pop("email", None)
    return {"message": "User logged out"}, 200


@app.route('/users')
@jwt_required()
def get_users():
    if index():
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            users = User.objects()
            return jsonify(users), 200
        return {'message': 'Profile not found'}, 404
    return {"message": "Please log in"}, 404


@app.route('/users/<id>')
@jwt_required()
def get_one_user(id: str):
    if index():
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        id = User.objects(id=id)
        if user and id:
            return jsonify(id), 200
        return {"message": "User id didn't match or user isn't authenticated"}, 404
    return {"message": "Please log in"}, 404


@app.route('/users/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    if index():
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        id = User.objects(id=id)
        if user and id:
            body = request.get_json()
            id.update(**body)
            return jsonify(id), 200
        return {"message": "User id didn't match"}, 404
    return {"message": "Please log in"}, 404


@app.route('/users/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    if index():
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        id = User.objects(id=id)
        if user and id:
            id.delete()
            return jsonify(id), 200
        return {"message": "User id didn't match"}, 404
    return {"message": "Please log in"}, 404


if __name__ == "__main__":
    app.run(debug=True, port=8888)
