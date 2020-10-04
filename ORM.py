from peewee import *

##db = SqliteDatabase('pepole.db')

# Connect to a MySQL database on network.
db = MySQLDatabase('my_app', user='root', password='112233sa',
                         host='localhost', port=3306)




class Person(Model):
    name = CharField()
    brthdate = DateField()

    class Meta:
        database = db  # This Model Use the "pepole db " database


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


db.connect()
db.create_tables([Person, Pet])
##db.create_tables([Pet])


