
from datetime import datetime
from models.db import db
# from models.user import User

class Dislikes(db.EmbeddedDocument):
    users = db.ListField(db.ReferenceField('User'))
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Dislikes, self).save(*args, **kwargs)