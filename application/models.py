from application import db
from datetime import datetime

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_title = db.Column(db.String(100), nullable = False)
    workout_created = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    exercises = db.relationship("Exercises", backref="Workout")
    

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercises_title = db.Column(db.String(100), nullable = False)
    exercise_created = db.Column(db.Boolean, nullable=False, default=False)
    workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), nullable=False)
    repetitions_number = db.Column(db.Integer, nullable=False)

    