from mongoengine import *
import datetime
#connect('db')

class DBHero(Document):
    tree = DictField()
    date_mod = DateTimeField(default=datetime.datetime.now)

class DBAchievements(Document):
    tree = ListField()
    date_mod = DateTimeField(default=datetime.datetime.now)

class DBTop_Heros(Document):
    tree = ListField()
    date_mod = DateTimeField(default=datetime.datetime.now)
