from django.urls import path
from chatApp.views import *

urlpatterns = [
    path("",create_room,name="create_room"),
    path("message/<str:room_name>/<str:username>/",message,name="message")
]
