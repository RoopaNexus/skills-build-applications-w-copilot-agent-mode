from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

client = MongoClient('localhost', 27017)
db = client['octofit_db']

class UserList(APIView):
    def get(self, request):
        users = list(db.users.find({}, {'_id': 0}))
        return Response(users)

class TeamList(APIView):
    def get(self, request):
        teams = list(db.teams.find({}, {'_id': 0}))
        return Response(teams)

class ActivityList(APIView):
    def get(self, request):
        activities = list(db.activities.find({}, {'_id': 0}))
        return Response(activities)

class LeaderboardList(APIView):
    def get(self, request):
        leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
        return Response(leaderboard)

class WorkoutList(APIView):
    def get(self, request):
        workouts = list(db.workouts.find({}, {'_id': 0}))
        return Response(workouts)
