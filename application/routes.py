from application import app, db
from application.models import Workout, exercises

@app.route("/")
@app.route("/home")
def home():
    all_workout = Workout.query.all()
    return str(all_workout)

@app.route("/create")
def create():
    new_workout = Workout("new workout added")
    db.session.add(new_workout)
    db.session.commit()
    return "new workout added"

@app.route("/exercise/<int:id>")
def exercise(id):
    workout = Workout.query.filter_by(id=id).first()
    workout.exercise_added = True
    db.session.commit()
    return f"Exercise {id} is now added"

@app.route("/repetitions/<int:id>")
def repetitions(id):
    workout = Workout.query.filter_by(id=id).first()
    workout.repetitions_added = True
    db.session.commit()
    return f"Repetitions is now added to {id}"

@app.route("/weight/<int:id>")
def weight(id):
    workout = Workout.query.filter_by(id=id).first()
    workout.weight_added = True
    db.session.commit()
    return f"weight is now added to {id}"

@app.route("/update/<new_exercise>")
def update(new_exercise):
    workout = Workout.query.order_by(workout.id.desc()).first()
    workout.exercise = new_exercise
    db.session.commit()
    return f"Most recent workout was updated with the exercise: {new_exercise}"

@app.route("/delete/<int:id>")
def delete(id):
    workout = Workout.query.filter_by(id=id).first()
    db.session.delete(workout)
    return f"workout {id} was deleted."
    