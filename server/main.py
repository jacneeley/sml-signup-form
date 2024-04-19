from flask import Flask, redirect ,url_for, request, json
from flask_cors import CORS, cross_origin
from utils.initApp import app, _build_cors_preflight_response, _corsify_actual_response
from utils.dbController import initDB, createUser, deleteUser, displayAll

CORS(app, resources={r"/attendees/*": {"origins": "*"},
                     r"/attendees/add": {"origins": "*"},
                     r"/attendees/del": {"origins": "*"}})

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

if __name__ == "__main__":
        app.run(debug=True)