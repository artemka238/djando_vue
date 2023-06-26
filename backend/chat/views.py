from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
# получаем данные с БД
# сериализуем данные
# отдаём ответ

class RoomAPI(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self,request):
        rooms = Room.objects.filter(Q(creator = request.user) | Q(invited = request.user))
        serializers = RoomSerializer(rooms, many = True)
        return Response({'data':serializers.data})
    
    def post(self,request):
        # сохранение записи с указателем 
        Room.objects.create(creator = request.user)
        return Response(status = 201)
    
class DialogAPI(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room = room)
        serializer = ChatSerializer(chat, many = True)
        return Response({'data':serializer.data})
    
    def post(self,request):
        # data - параметр для всех данных
        print(request.data)
        dialog = ChatPostSerializer(data = request.data)
        # print(dialog.errors)
        if dialog.is_valid():
            # save - сохранение записи
            dialog.save(user = request.user)
            return Response(status = 201)
        else:
            print(dialog.errors)
            return Response(status = 400)
        

class AddUserRoomAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializers(users, many = True)
        return Response({'data':serializers.data})
    
    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')

        try: 
            room = Room.objects.get(id = room)
            room.invited.add(user)
            room.save()
            return Response(status = 201)

        except:
            return Response(status = 400)
