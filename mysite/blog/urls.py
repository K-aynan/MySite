from django.urls import re_path
from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]