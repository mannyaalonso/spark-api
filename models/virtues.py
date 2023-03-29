from datetime import datetime
from models.db import db


class Virtues(db.EmbeddedDocument):
    work = db.StringField()
    work_visibility = db.BooleanField()
    job_title = db.StringField()
    job_title_visibility = db.BooleanField()
    school = db.StringField()
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
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Virtues, self).save(*args, **kwargs)
