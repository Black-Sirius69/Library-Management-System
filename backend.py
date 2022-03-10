import sqlalchemy
from sqlalchemy import Column, Table, ForeignKey, Date
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

Book = Base.classes.books
Students = Base.classes.students
t_issues = Table(
    'issues', Base.metadata,
    Column('book_no', ForeignKey('books.Acc_no', ondelete='CASCADE', onupdate='CASCADE'), index=True, comment='The Accession number of the book issued'),
    Column('student_id', ForeignKey('students.Admno', ondelete='CASCADE', onupdate='CASCADE'), index=True, comment='The Admission Number of the student who is issuing the book'),
    Column('issue_date', Date, comment='The date of issuing the book'),
    Column('return_date', Date, comment='The date of returning the book'),
    comment='A table for storing info of issued books',
    extend_existing = True
)

# Create a session
session = Session(engine)
