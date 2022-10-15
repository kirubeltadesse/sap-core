from django.urls import path 
from .views import EventDetail, EventList# type: ignore

app_name = 'api'

urlpatterns = [
    path('<int:pk>/', EventDetail.as_view(), name='detail'),
    path('', EventList.as_view(), name='list'),

]
