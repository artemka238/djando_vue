from django.urls import path
from . import views

urlpatterns = [
    path("tasks",views.task),
    path("tasks/<int:pk>/",views.task_detale)
]
