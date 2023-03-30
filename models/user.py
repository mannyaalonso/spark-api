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
from mongoengine import *


class User(db.Document):
    email = db.StringField()
    password = db.BinaryField()
    location = db.PointField(auto_index=False)
    location_visibility = db.BooleanField()
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

    meta = {
        'indexes': [[("location", "2dsphere")]]
    }

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(User, self).save(*args, **kwargs)
