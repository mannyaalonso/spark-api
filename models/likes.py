from datetime import datetime
from models.db import db


class Likes(db.EmbeddedDocument):
    users = db.ListField(db.ReferenceField('User'))
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Likes, self).save(*args, **kwargs)