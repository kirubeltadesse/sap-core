from django.urls import path 
# from .views import PostList, PostDetail
from django.views.generic import TemplateView

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('', PostList.as_view(), name='listcreate'),
    path('', TemplateView.as_view(template_name='api/index.html')),
]
