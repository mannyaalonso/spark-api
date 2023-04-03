from datetime import datetime
from models.db import db


class Vitals(db.EmbeddedDocument):
    first_name = db.StringField()
    last_name = db.StringField()
    gender = db.StringField()
    gender_visibility = db.BooleanField()
    pronouns = db.ListField(db.StringField())
    pronouns_visibility = db.BooleanField()
    sexuality = db.StringField()
    sexuality_visibility = db.BooleanField()
    age = db.StringField()
    age_update = db.IntField(default=0)
    age_visibility = db.BooleanField()
    height = db.StringField()
    height_visibility = db.BooleanField()
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
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Vitals, self).save(*args, **kwargs)
