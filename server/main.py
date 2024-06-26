from flask import Flask, redirect ,url_for, request, jsonify
from flask_cors import CORS, cross_origin
from utils.initApp import app
from utils.dbController import initDB, createUser, deleteUser, displayAll
from utils.auth import auth

CORS(app, resources={r"/attendees/*": {"origins": "*"},
                     r"/attendees/add": {"origins": "*"},
                     r"/attendees/del": {"origins": "*"},
                     r"/auth/": {"origins": "*"}})

with app.app_context():
        initDB()

@app.route("/")
def index():
        return redirect(url_for('attendees'))

@app.route("/attendees/", methods=['GET'], strict_slashes=False)
def attendees():
        return displayAll()
    
@app.route("/attendees/add/", methods=['GET','POST'], strict_slashes=False)
def add_attendees():
        user = request.get_json()
        print(user)
        createUser(user)
        return redirect(url_for('attendees'))

@app.route("/attendees/del/<int:id>", methods=['GET','POST'], strict_slashes=False)
def del_attendees(id):
        deleteUser(id)
        return redirect(url_for('attendees'))

@app.route("/auth/", methods=['POST'], strict_slashes=False)
def authenticate():
        admin = request.get_json()
        return auth(admin)


if __name__ == "__main__":
        app.run(debug=True)