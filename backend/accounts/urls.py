from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r"users",views.UserViewSet)

urlpatterns = [
    path("",include(router.urls)),
    path("token/",jwt_views.TokenObtainPairView.as_view(),name = "token_obtain_pair"),
    path("token/refresh/",jwt_views.TokenRefreshView.as_view(),name = "token_refresh"),
    # path("user/create/",views.UserRegistration.as_view(),name = "create_user")
]
