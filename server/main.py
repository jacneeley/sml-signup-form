from flask import Flask, redirect ,url_for, json
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from utils.dbController import initDB

app=Flask(__name__)
CORS(app, resources={r"/attendees/": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)    
#db.init_app(app)

initDB(app,db)

@app.route("/")
def index():
        return redirect(url_for('attendees'))

@app.route("/attendees/", methods=['GET'])
def attendees():
        return "<html>Attendees</html>"
    
# @app.route("/attendees/add", methods=['POST'])
# def add_attendees():
#         return 

if __name__ == "__main__":
        app.run(debug=True)