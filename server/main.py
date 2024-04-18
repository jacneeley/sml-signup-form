from flask import Flask, redirect ,url_for, json
from flask_cors import CORS, cross_origin
from utils.initApp import app
from utils.dbController import initDB, deleteUser, displayAll

CORS(app, resources={r"/attendees/": {"origins": "*"}})

with app.app_context():
        initDB()
        print(displayAll())

@app.route("/")
def index():
        return redirect(url_for('attendees'))

@app.route("/attendees/", methods=['GET'])
def attendees():
        return displayAll()
    
# @app.route("/attendees/add/", methods=['POST'])
# def add_attendees():
#         return 

@app.route("/attendees/del/", methods=['GET'])
def del_attendees():
        deleteUser(1)
        return redirect(url_for('attendees'))

if __name__ == "__main__":
        app.run(debug=True)