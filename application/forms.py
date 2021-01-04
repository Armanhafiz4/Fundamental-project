from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class WorkoutForm(FlaskForm):
    workout_title = StringField('Title of the Workout:', validators = [DataRequired()])
    submit = SubmitField('Add Workout')

class ExerciseForm(FlaskForm):
    workout_title = StringField('Title of the Workout', validators = [DataRequired()])
    workout_id = StringField('Title of the main workout', validators = [DataRequired()])
    exercise_title = StringField('Title of Exercise:', validators = [DataRequired()])
    title = StringField('Title of the Exercise:', validators = [DataRequired()])
    repetitions = StringField('Number of repetitions:', validators = [DataRequired()])
    submit = SubmitField('Add Workout') 

