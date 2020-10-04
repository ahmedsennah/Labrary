from peewee import *
import datetime 
db = MySQLDatabase('library', user='root',password='112233sa',
                           host='localhost', port=3306)

##db = MySQLDatabase(
  #  database='library',
   # user='root',
    #password='112233sa',
    #host='localhost',
    #port = '3306'

#)

db.connect()




class Category(Model):
    Category_name = CharField(unique=True)
    parent_Category = IntegerField(null=True)  # Recursvie Relation
    class Meta:
        database = db  # This Model Use the "pepole db " database


class Branch(Model):
    name = CharField()
    code = CharField(null=True, unique=True)
    Location = CharField(null=True)
    class Meta:
        database = db  # This Model Use the "pepole db " database


class Puplisher (Model):
    name = CharField(unique=True)
    location = CharField(null=True)
    class Meta:
        database = db  # This Model Use the "pepole db " database


class Author (Model):
    name = CharField(unique=True)
    location = CharField(null=True)
    class Meta:
        database = db  # This Model Use the "pepole db " database

BOOK_SATAUS = (
    (1,'NEW'),
    (2,'USED'),
    (3,'DAMAGED')
    )


class Books(Model):
    title = CharField(unique = True)
    descriotion=TextField(null= True)
    category = ForeignKeyField(Category, backref='category', null=True)
    code=CharField(null = True)
    parcode = CharField(unique = True)
    #*part*
    part_Order = IntegerField(null=True )
    price = DecimalField(null = True)
    puplisher = ForeignKeyField(Puplisher, backref='puplisher' , null = True )
    auther = ForeignKeyField(Author, backref='author')
    image = CharField(null = True)
    status =  CharField(choices = BOOK_SATAUS)
    date = DateTimeField(default = datetime.datetime.now )
    class Meta:
        database = db  # This Model Use the "pepole db " database


class Clients(Model):
    name = CharField()
    mail = CharField(null=True, unique=True)
    phone = CharField (null = True)
    date = DateTimeField(default=datetime.datetime.now)
    national_ID = IntegerField(null=True, unique=True , default = datetime.datetime.now )
    class Meta:
        database = db  # This Model Use the "pepole db " database


class Employee(Model):
    name = CharField()
    mail = CharField(null=True, unique=True)
    phone = CharField (null = True)
    date = DateTimeField(default = datetime.datetime.now )
    national_ID = IntegerField(null=True, unique=True)
    periority = IntegerField(null=True)
    #permissions = IntegerField()
    class Meta:
        database = db  # This Model Use the "pepole db " database

PROCESS_TYPE = (
    (1,'RENT'),
    (2,'RETRIVE')
    
)



class Daily_Movment(Model):
    book= ForeignKeyField(Books,backref='daily_books')
    client = ForeignKeyField(Clients, backref='book_client')
    type_daily = CharField(choices = PROCESS_TYPE)  # (rent - retrive)
    date = DateTimeField(default=datetime.datetime.now)
    barnch = ForeignKeyField(Branch, backref='Daily_branch', null=True)
    book_from = DateField(null = True)
    book_to = DateField(null=True)
    employee = ForeignKeyField(Employee, backref='Daily_emplyee', null=True)
    class Meta:
        database = db  # This Model Use the "pepole db " database

ACTION_TYPE = (
    (1,'Login'),
    (2,'Update'),
    (3,'Create'),
    (4,'Delete')
)


TABLE_CHOICES = (
    (1,'Books'),
    (2,'Cleint'),
    (3,'Employee'),
    (4,'Category'),
    (5,'Branch'),
    (6,'Daily_Movment'),
    (7,'Puplisher'),
    (8,'Aothor')
    
)

class History(Model):
    employee= ForeignKeyField(Employee, backref='history_employee')
    action = CharField(choices = ACTION_TYPE)# choices
    table = CharField()  # choices
    date=DateTimeField()
    branch= ForeignKeyField(Branch, backref='branch')
    class Meta:
        database = db  # This Model Use the "pepole db " database



db.connect
db.create_tables([Category, Branch, Puplisher, Author, Books,Clients, Employee, Daily_Movment, History])













