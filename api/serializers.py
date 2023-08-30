from dataclasses import fields
from rest_framework import serializers
from backend.models import Event, Mainuser, Student, Mentor

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'content', 'student', 'mentor', 'start_date', 'end_date', 'status')

# the student class

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainuser 
        fields = ('__all__')

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('__all__')
