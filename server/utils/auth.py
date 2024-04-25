import json
from sqlalchemy.sql import exists
from sqlalchemy import and_
from .initApp import db
from .dbController import User

def auth(admin):
    print(admin['email'], admin['phone'])
    admin_exists = db.session.query(User).filter(User.email == admin['email']).first()
    print(admin_exists)
    if admin_exists:
        return "1"
    else:
        return "0"