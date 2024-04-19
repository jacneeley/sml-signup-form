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

    def __init__(self, email, parentName, phone, childName, childAge):
        self.email = email
        self.parentName = parentName
        self.phone = phone
        self.childName = childName
        self.childAge = childAge
        
    def __repr__(self):
        return "<User: (email='%s', parentName='%s', phone='%s', childName='%s', childAge='%s')>" % (
            self.email, self.parentName, self.phone, self.childName, self.childAge)


class UserSchema(Schema):
    _id = fields.Integer()
    email = fields.String()
    parentName = fields.String()
    phone = fields.String()
    childName = fields.String()
    childAge = fields.Integer()


def initDB():
    #create instance
    db.create_all()
        
    #check if admin user already exists, if not add admin
    if db.session.query(exists().where(User.email == "admin@test.com")).scalar() is False:
        print("setting up DB...")
        usr = User("admin@test.com", "Admin", "999-999-9988", "Jacob Neeley", 23)

        db.session.add(usr)
        db.session.commit()
        
        print("Done.")
    else:
        print("db found!")


def createUser(user):
    # user = {
    #     "email" : "test@test.com",
    #     "parentName" : "test test",
    #     "phone": "999-999-9999",
    #     "childName": "Test Test",
    #     "childAge": 12
    # }
    
    addUser = User(addUser.get("email"), addUser.get("parentName"), user.get("phone"), user.get("childName"), user.get("childAge"))
    
    db.session.add(addUser)
    db.session.commit()


def deleteUser(id):
    if db.session.query(exists().where(User._id == id)).scalar() is True:
        delUser = db.get_or_404(User,id)
        db.session.delete(delUser)
        db.session.commit()
        print("User has been permanently deleted.")
    else:
        print("User does not exist")

   
def displayAll():
    user_schema = UserSchema()
    user_data = db.session.query(User).all()
    json_output = json.loads(user_schema.dumps(user_data, many=True))
    return json_output