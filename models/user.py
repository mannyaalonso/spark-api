from datetime import datetime
from models.db import db
from models.likes import Likes
from models.dislikes import Dislikes
from models.preferences import Preferences
from models.pictures import Pictures
from models.prompts import Prompts
from models.virtues import Virtues
from models.vitals import Vitals
from models.vices import Vices


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
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(User, self).save(*args, **kwargs)
