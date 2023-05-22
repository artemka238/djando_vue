from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes,action
from rest_framework.renderers import JSONRenderer
# from .serializers import UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)

# @api_view(["POST"])
# def create_user(request):
#     serializer = UserSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {
#             "data":serializer.data
#             },
#             status = status.HTTP_201_CREATED
#         )
#     return Response(
#             {
#             "data":serializer.errors
#             },
#             status = status.HTTP_400_BAD_REQUEST
#         )

# class UserRegistration(APIView):
#     permission_classes = (AllowAny,)#что бы было не только для тех кто авторизован
#     def post(self,request,format = "json",*args,**kwargs):
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                 "data":serializer.data
#                 },
#                 status = status.HTTP_201_CREATED
#             )
#         return Response(
#                 {
#                 "data":serializer.errors
#                 },
#                 status = status.HTTP_400_BAD_REQUEST
#             )

# class UserViewSet(ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @action(methods=["post"], detail=False)
#     def register(self,request):
#         data = {
#             "username":request.data.get("username"),
#             "password":make_password(request.data.get("password"))
#         }

#         print(make_password(request.data.get("password")))

#         serializer = self.get_serializer(data = data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED
#             )
    
# class UserDetailView(APIView):
#     def get_user(self,id):
#         try:
#             user = User.objects.get(id = id)
#             return user
        
#         except User.DoesNotExist:
#             return None
        
#     def get(self,request,id):
#         user = self.get_user(id)
#         if(user is None):
#             return Response(status = status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
class ObtainJsonWebTokenEmail(ObtainJSONWebToken): # получение токена jwt
    def post(self, request, *args, **kwargs):
        if 'email' in request.data: # проверяем есть ли почта в запросе
            try: # пытаемся найти запись в БД с такой почтой 
                user = User.objects.get(email = request.data['email'])
            except User.DoesNotExist: # если не нашли
                user = None

        if user: # если нашли
            del request.data['email'] # удаляем почту из запроса 
            request.data['username'] = user.username # добавляем данные пользователя в запрос
        return super().post(request, *args, **kwargs) # передаём новые данные родителю класса


class RefreshJsonWebTokenEmail(RefreshJSONWebToken): # обновление токена jwt
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 400:
            return Response({
                'status':'nok'
            })
        return response
