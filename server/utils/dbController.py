from sqlalchemy.sql import exists
from marshmallow import Schema, fields
import os, json
from .initApp import db

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    email = db.Column("email",db.String(100))
    parentName = db.Column("parentName",db.String(100))
    phone = db.Column("phone",db.String(12))
    childName = db.Column("childName",db.String(100))
    childAge = db.Column("childAge",db.Integer)
    laptop = db.Column("laptop", db.String(3))

    def __init__(self, email, parentName, phone, childName, childAge, hasLaptop):
        self.email = email
        self.parentName = parentName
        self.phone = phone
        self.childName = childName
        self.childAge = childAge
        self.laptop = hasLaptop
        
    def __repr__(self):
        return "<User: (email='%s', parentName='%s', phone='%s', childName='%s', childAge='%s', hasLaptop='%s')>" % (
            self.email, self.parentName, self.phone, self.childName, self.childAge, self.laptop)


class UserSchema(Schema):
    _id = fields.Integer()
    email = fields.String()
    parentName = fields.String()
    phone = fields.String()
    childName = fields.String()
    childAge = fields.Integer()
    laptop = fields.String()


def initDB() -> None:
    #create instance
    db.create_all()
        
    #check if admin user already exists, if not add admin
    if db.session.query(exists().where(User.email == "admin@test.com")).scalar() is False:
        print("setting up DB...")
        usr = User(
            "admin@test.com",
            "Admin",
            "999-999-9999",
            "Mr. Admin",
            25,
            "Yes"
        )

        db.session.add(usr)
        db.session.commit()
        
        print("Done.")
    else:
        print("db found!")


def createUser(user:dict) -> None:    
    addUser = User(
        user.get("email"),
        user.get("parentName"),
        user.get("parentPhone"),
        user.get("childName"),
        user.get("childAge"),
        user.get("laptop")
    )
    
    db.session.add(addUser)
    db.session.commit()


def deleteUser(id: int) -> None:
    if db.session.query(exists().where(User._id == id)).scalar() is True:
        delUser = db.get_or_404(User,id)
        db.session.delete(delUser)
        db.session.commit()
        print("User has been permanently deleted.")
    else:
        print("User does not exist")

   
def displayAll() -> dict:
    user_schema = UserSchema()
    user_data = db.session.query(User).all()
    json_output = json.loads(user_schema.dumps(user_data, many=True))
    return json_output