import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Workout, Exercises

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_workout = Workout(workout_title="Workout1")
        db.session.add(test_workout)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_createworkout_get(self):
        response = self.client.get(url_for('createworkout'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_workout(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Workout1", response.data)

class TestCreateworkout(TestBase):
    def test_createworkout_workout(self):
        response = self.client.post(
            url_for('createworkout'),
            data=dict(workout_title="Create A Workout"),
            follow_redirects=True  
        )
        self.assertIn(b"Create A Workout", response.data) 

class TestUpdate(TestBase):
    def test_update_workout(self):
        response = self.client.post(
            url_for("update", id=1), 
            data = dict(workout_title = "Update A Workout"), 
            follow_redirects=True
        )
        self.assertIn(b"Update A Workout", response.data)

class TestDelete(TestBase):
    def test_delete_workout(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Workout1", response.data) 