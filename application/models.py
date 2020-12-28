from application import db
from datetime import datetime

class workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_the_week = db.Column(db.String(9), nullable=False)
    date_created = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    exercises = db.relationship("exercises", backref="workout")

class exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    weight_used = db.Column(db.Integer, nullable=False)



    