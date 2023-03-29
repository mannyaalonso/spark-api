from datetime import datetime
from models.db import db


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
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Preferences, self).save(*args, **kwargs)