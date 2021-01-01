from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class WorkoutForm(FlaskForm):
    workout_title = StringField('Title of the Workout:', validators = [DataRequired()])
    exercises_title = StringField('Title of Exercise:', validators = [DataRequired()])
    repetitions = StringField('Number of repetitions:', validators = [DataRequired()])
    submit = SubmitField('Add Workout')

class ExerciseForm(FlaskForm):
    workout_title = StringField('Title of the Workout', validators = [DataRequired()])
    submit = SubmitField('Add Exercise') 

