from rest_framework import serializers
from backend.models import Event, Student

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'content', 'student', 'mentor', 'start_date', 'end_date', 'status')

# the student class

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name','last_name','email')

