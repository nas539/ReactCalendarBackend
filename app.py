from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sfpidbnchhmftd:a66a9d829a0e814a66837d4f9285de8f86a3262efb6e27f33425ffed05035fff@ec2-34-230-231-71.compute-1.amazonaws.com:5432/ddng22t6uds9fs"

db = SQLAlchemy(app)
ma = Marshmallow(app)
heroku = Heroku(app)
CORS(app)


class Month(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, unique=True, nullable=False)
    month = db.Column(db.String, nullable=False)
    daysInMonth = db.Column(db.Integer, nullable=False)
    daysInPreviousMonth = db.Column(db.Integer, nullable=False)
    startDay = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self, position, month, daysInMonth, daysInPreviousMonth, startDay, year):
        self.position = position
        self.month = month
        self.daysInMonth= daysInMonth
        self.daysInPreviousMonth = daysInPreviousMonth
        self.startDay = startDay
        self.year = year

class MonthSchema(ma.Schema):
    class Meta:
        fields = ("id", "position", "month", "daysInMonth", "daysInPreviousMonth", "startDay", "year")


month_schema = MonthSchema()
months_schema = MonthSchema(many=True)

if __name__ == "__main__":
    app.debug = True
    app.run()