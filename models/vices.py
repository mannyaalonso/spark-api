from datetime import datetime
from models.db import db


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
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Vices, self).save(*args, **kwargs)
