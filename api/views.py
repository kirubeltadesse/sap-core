from rest_framework import generics
from backend.models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.eventobjects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
