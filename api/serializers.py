from rest_framework import serializers
from backend.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'content', 'student', 'mentor', 'start_date', 'end_date', 'status')