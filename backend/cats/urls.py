from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('cats/',views.CatsAPI.as_view()),
    path("search",views.SearchCat),
    path("add/",views.CatAdding),
    path("info/",views.GetUserInfo.as_view())
]
