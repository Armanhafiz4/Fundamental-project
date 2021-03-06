from application import app, db
from application.models import Workout, Exercises
from application.forms import WorkoutForm, ExerciseForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_workouts = Workout.query.all() 
    all_exercises = Exercises.query.all()         
    return render_template("index.html", title="Home", all_workouts=all_workouts, all_exercises=all_exercises) 

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

@app.route("/create_exercise/<int:id>", methods=['GET','POST'])
def create_exercise(id):
    form = ExerciseForm()
    all_exercises = Exercises.query.filter_by(id=id).all() 
    if request.method == 'POST':
            new_exercise = Exercises(exercise_title=form.exercise_title.data, id=id)
            db.session.add(new_exercise)
            db.session.commit()
            return redirect(url_for("home")) 
    return render_template("add_exercise.html", title="Add an Exercise", form=form, all_exercises=all_exercises)

@app.route("/update/<int:id>", methods = ["GET", "POST"])             
def update(id):
    form = WorkoutForm()
    if request.method == "POST":
        workout = Workout.query.filter_by(id=id).first()
        workout.workout_title = form.workout_title.data   
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("update.html", title="Update Workout",form=form)

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def delete(id):
    form = WorkoutForm()
    workouts = Workout.query.filter_by(id=id).first()
    db.session.delete(workouts)
    db.session.commit()
    return redirect(url_for("home")) 