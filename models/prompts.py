from datetime import datetime
from models.db import db


class Prompts(db.EmbeddedDocument):
    prompt_1 = db.StringField()
    answer_1 = db.StringField()
    visible_1 = db.BooleanField()
    prompt_2 = db.StringField()
    answer_2 = db.StringField()
    visible_2 = db.BooleanField()
    prompt_3 = db.StringField()
    answer_3 = db.StringField()
    visible_3 = db.BooleanField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Prompts, self).save(*args, **kwargs)