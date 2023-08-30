from rest_framework import generics
from backend.models import Event, Mainuser
from .serializers import EventSerializer, MentorSerializer, MainSerializer, StudentSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.eventobjects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MainList(generics.ListCreateAPIView):
    queryset = Mainuser.objects.all()
    serializer_class = MainSerializer
