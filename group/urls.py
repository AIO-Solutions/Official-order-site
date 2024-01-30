from django.urls import path
from .views import *
urlpatterns=[
    path("team/",team,name='team'),
    path("media/<path:file_path>/",serve_media,name="serve_media"),
]