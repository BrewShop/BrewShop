#python 3.8
import json
from flask import Flask, jsonify # add package for web servers to the program
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__) # start up a web server instance
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '470154729788964',
        'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}

CORS(app)

db = SQLAlchemy(app)
lm = LoginManager(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))



@app.route('/allBrew', methods=['GET', 'POST']) # navigating to localhost:5000/allBrew will return all brews
def allBrew():
    f = open("list0.json") #open list0.json
    return jsonify(json.load(f)) #send the files' contents to the client

@app.route('/byCat', methods=['GET', 'POST'])
def byCat():
    shit = json.load(open("list0.json"))
    res = {"all":[], "apps":[], "games":[],"emulator":[], "other":[]}
    for turd in shit:
        val = {"author":"","create_time":0,"description":"","id":0,"name":"","titleid":"","update_time":"","url":"","version":0} 
        try:
            val["author"] = turd["author"]
            val["create_time"]= turd["create_time"]
            val["description"]= turd["description"]
            val["id"]= turd["id"]
            val["name"]= turd["name"]
            val["titleid"]= turd["titleid"]
            val["update_time"]= turd["update_time"]
            val["url"]= turd["url"]
            val["version"]= turd["version"]
        except Exception:
            print("error")

        if(1 in turd["categories"]):
            res["all"].append(val)
        if(2 in turd["categories"]):
            res["apps"].append(val)
        if(3 in turd["categories"]):
            res["games"].append(val)
        if(4 in turd["categories"]):
            res["emulator"].append(val)
        if(5 in turd["categories"]):
            res["other"].append(val)

    return jsonify(res)


if __name__ == '__main__': #start the application (usefull for debugging)
    app.run()

# python app.py 
# make sure list0.json is in the directory
# use your browser and go to localhost:5000/allBrew