from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('cats/',views.CatsAPI.as_view()),
    path('cats/buy/',views.CatsBuyAPI.as_view()),
    path("search",views.SearchCat),
    path("add/",views.CatAdding),
    path("info/",views.GetUserInfo.as_view()),
    path('cats_shop/',views.CatShopAPI.as_view()),
    path('cat_history/',views.UserHistoryAPI.as_view()),
]
