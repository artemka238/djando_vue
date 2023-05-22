from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path("room/",views.RoomAPI.as_view()),
    path("dialog/",views.DialogAPI.as_view()),
    path("users/",views.AddUserRoomAPI.as_view())
]
