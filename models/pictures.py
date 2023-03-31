from datetime import datetime
from models.db import db


class Pictures(db.EmbeddedDocument):
    titles = db.ListField()
    images = db.ListField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Pictures, self).save(*args, **kwargs)