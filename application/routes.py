from application import app, db
from application.models import workout, exercises

@app.route("/")
@app.route("/home")
def home():
    all_workout = workout.query.all()
    all_exercise = exercise.query.all()
    return str(all_workout)
    return str(all_exercise)

@app.route("/create")
def create():
    new_workoutday = workout(description = "new workout")
    db.session.add(new_workout)
    db.session.commit()
    return "new workout added"
    