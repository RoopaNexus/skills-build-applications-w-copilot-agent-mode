from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import settings

from django.db import connection

# Define models inline for demonstration; in real app, use models.py
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email
        db.users.create_index('email', unique=True)

        # Users (superheroes)
        users = [
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "dc"},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {"name": "marvel"},
            {"name": "dc"},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "Tony Stark", "activity_type": "Running", "duration": 30, "team": "marvel"},
            {"user": "Steve Rogers", "activity_type": "Cycling", "duration": 45, "team": "marvel"},
            {"user": "Bruce Wayne", "activity_type": "Swimming", "duration": 25, "team": "dc"},
            {"user": "Clark Kent", "activity_type": "Flying", "duration": 60, "team": "dc"},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"user": "Tony Stark", "team": "marvel", "points": 100},
            {"user": "Steve Rogers", "team": "marvel", "points": 90},
            {"user": "Bruce Wayne", "team": "dc", "points": 95},
            {"user": "Clark Kent", "team": "dc", "points": 110},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"name": "Super Strength", "description": "Strength training for heroes.", "suggested_for": "marvel"},
            {"name": "Flight School", "description": "Aerobic flying workouts.", "suggested_for": "dc"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
