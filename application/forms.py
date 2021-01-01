from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class WorkoutForm(FlaskForm):
    workout_title = StringField('Title of the Workout', validators = [DataRequired()])
    submit = SubmitField('Add Workout')

class ExerciseForm(FlaskForm):
    workout_title = StringField('Title of the Workout', validators = [DataRequired()])
    exercise_title = StringField('Title of the Exercise', validators = [DataRequired()])
    created = BooleanField('Do you want this exercise to be added in your workout')
    repetition = StringField('How many times would you like to do this exercise', validators = [DataRequired()])
    submit = SubmitField('Add Exercise') 

