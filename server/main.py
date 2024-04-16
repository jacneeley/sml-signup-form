from flask import Flask, redirect ,url_for, json
from flask_cors import CORS, cross_origin
from utils.handleData import attendees_json

app=Flask(__name__)
CORS(app, resources={r"/albums/*": {"origins": "*"}})

@app.route("/")
def index():
    return redirect(url_for('attendees'))

@app.route("/attendees/", methods=['GET'])
def attendees():
        return attendees_json

if __name__ == "__main__":
    app.run(debug=True)