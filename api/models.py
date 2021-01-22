from mongoengine import *

import datetime
connect('clij')

class User(Document):
  extId = StringField(required=True, unique=True)
  name = StringField(required=True)
  selectedJournal = ReferenceField('Journal')

class Journal(Document):
  userId = ReferenceField('User')
  title = StringField(required=True, max_length=200)
  entryIds = ListField()

class Entry(Document):
    userId = ReferenceField('User')
    journalId = ReferenceField('Journal')
    category = StringField(required=True, max_length=200)
    content = StringField(required=True)
    datetime = DateTimeField(default=datetime.datetime.now)
