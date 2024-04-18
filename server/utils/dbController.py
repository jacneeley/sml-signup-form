from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def initDB(app,db):
    with app.app_context():
        class User(db.Model):
            _id = db.Column("id", db.Integer, primary_key = True)
            email = db.Column(db.String(100), unique = True)
            parentName = db.Column(db.String(100))
            phone = db.Column(db.String(12))
            childName = db.Column(db.String(100))
            childAge = db.Column(db.Integer)

            def __init__(self, email, parentName, phone, childName, childAge):
                self.email = email
                self.parentName = parentName
                self.phone = phone
                self.childName = childName
                self.childAge = childAge
                
            def __str__(self):
                return "<User(email='%s', parentName='%s', phone='%s', childName='%s', childAge='%s')>" % (
                    self.email, self.parentName, self.phone, self.childName, self.childAge)
        
        #create user and insert into table
        
        db.create_all()
        
        usr = User("admin@test.com", "Admin", "999-999-9988", "Jacob Neeley", 23)

        db.session.add(usr)
        db.session.commit()

        q = db.session.execute(db.select(User).order_by(User._id)).scalars().first()
        print(q)

        delUser = db.get_or_404(User,1)
        db.session.delete(delUser)
        db.session.commit()