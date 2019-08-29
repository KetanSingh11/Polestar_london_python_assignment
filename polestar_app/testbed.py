from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp.db"
db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    # dept_id = db.relationship("department", backref="dept")
    dept_id = db.Column(db.Integer, db.ForeignKey("department.id"))

    # Relationships
    dept = db.relationship("Department", backref="department")
