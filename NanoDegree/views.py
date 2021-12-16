import sqlalchemy
import datetime

# set up database
engine = sqlalchemy.create_engine('sqlite:///students.db', echo=True)
connection = engine.connect()
metadata = sqlalchemy.MetaData()
metadata.bind = engine
connection.bind = engine
metadata.create_all(engine)


# set up tables
students = sqlalchemy.Table('students', metadata,
                            sqlalchemy.Column(
                                'id', sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column('name', sqlalchemy.String),
                            sqlalchemy.Column('gpa', sqlalchemy.Float),
                            sqlalchemy.Column('birthday', sqlalchemy.Date)
                            )


students.create()

# insert data
insert = students.insert()
insert.execute(
    {'name': 'Michael', 'gpa': 2.5, 'birthday': datetime.date(2000, 1, 1)},
    {'name': 'Bob', 'gpa': 3.5, 'birthday': datetime.date(2020, 1, 1)},
    {'name': 'Alice', 'gpa': 4.5, 'birthday': datetime.date(2030, 1, 1)},
    {'name': 'John', 'gpa': 2.5, 'birthday': datetime.date(2040, 1, 1)},
    {'name': 'Mark', 'gpa': 3.5, 'birthday': datetime.date(2050, 1, 1)},
    {'name': 'Linda', 'gpa': 4.5, 'birthday': datetime.date(2060, 1, 1)},
)


# select data
result = connection.execute(students.select())
for row in result:
    print(row)
