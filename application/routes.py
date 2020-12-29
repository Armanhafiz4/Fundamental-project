from application import app, db
from application.models import Workout, Exercises
from application.forms import ExerciseForm, WorkoutForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_workouts = Workout.query.all()
    all_exercises = Exercises.query.all()           
    return render_template("index.html", title="Home", all_workouts=all_workouts, all_exercises=all_exercises)

@app.route("/create", methods = ["GET", "POST"])                       
def create():
    form = ExerciseForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_exercise = Exercise(exercise_title=form.exercise_title.data)
            db.session.add(new_exercise)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create an exercise", form=form)

@app.route("/createworkout", methods = ["GET", "POST"])
def createworkout():
    form = WorkoutForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_workout = Workout(workout_title=form.workout_title.data) 
            db.session.add(new_workout)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template ("add.html", title="Create a workout", form=form)

@app.route("/update/<int:id>", methods = ["GET", "POST"])             
def update(id):
    form = ExerciseForm()
    exercises = Exercises.query.filter_by(id=id).first()
    if request.method == "POST":
        exercise.title = form.title.data
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("update.html", form=form, title="Update Exercises")

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    book = Books.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home")) 