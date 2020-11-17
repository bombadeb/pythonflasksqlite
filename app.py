from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#USE URL not URL
# CTL + SHIF + P for sqlite
# LHS = Name of the column
# RHS = Actual value
# Name of the column = Actual value

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/<name>/<location>')
def index(name,location):
    user = User(name=name,location=location)
    db.session.add(user)
    db.session.commit()

    return '<h1> Added new user! </h1>'

@app.route('/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()

    return f'The user is located in: { user.location }'

@app.route('/delete/<name>')
def delete_user(name):
    user = User.query.filter_by(name=name).first()
    db.session.delete(user)
    db.session.commit()

    return f'The user { user.name} is located in: { user.location } is deleted!'


@app.route('/update/<name>/<location>')
def update_user(name,location):
    user = User.query.filter_by(name=name).first()
    user.location = location
    db.session.commit()

    return f'The user { user.name} is located in: { user.location } is Updated !!'


if __name__ == "__main__":
    app.run(debug=True)

