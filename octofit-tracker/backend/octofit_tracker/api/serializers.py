from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    team = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    team = serializers.CharField(max_length=100)

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    team = serializers.CharField(max_length=100)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    suggested_for = serializers.CharField(max_length=100)
