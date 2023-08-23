from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated
from rest_framework.response import Response
from cats.forms import CatsSearch, CatsForm
from django.db.models import Q

class CatsPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        cats = CatsForPeople.objects.filter(owner = request.user).count()
        print(cats)
        if cats > 0 and request.user and request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        cats = CatsForPeople.objects.filter(owner = request.user).count()
        print(cats)
        if cats > 0:
            return True
        return False


class CatsAPI(APIView):
    permission_classes = [CatsPermission]

    def get(self,request):
        cats = AboutCats.objects.all()
        serializers = CatsSerializers(cats, many = True)
        # print(serializers.data)
        return Response({'data':serializers.data})
    
    def post(self,request):
        cats = CatsSerializers(data = request.data)
        # print(dialog.errors)
        if cats.is_valid(): 
            cats.save()
            return Response(status=201)
        else:
            print(cats.errors)
            return Response(status = 400)
        
    
def GetCats(request):
    # catscats = AboutCats.objects.order_by("-age")
    catscats = AboutCats.objects.all()
    # catscats = AboutCats.objects.filter(age = 1)
    # catscats = AboutCats.objects.all().count()
    # catscats = AboutCats.objects.filter(breed = "scotland")
    # catscats = AboutCats.objects.filter(name = "abdul")   
    print(catscats)
    return render(request,'index.html', {'catscatscats':catscats})

def SearchCat(request):
    form = CatsSearch()
    result = []
    text = None
    if request.method == "GET":
        form = CatsSearch(request.GET)
        if form.is_valid():
            text = form.cleaned_data["name"]
            print(text)
            result = AboutCats.objects.filter(Q(name = text) | Q(breed = text))
            print(result)


    return render(request,'catSearch.html',{'form':form, 'result':result, "text":text})

def CatAdding(request):
    if request.method == "POST":
        form = CatsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('its ok')
        else:
            print(form.errors)
    else:
        form = CatsForm()

    return render(request,'catIndex.html',{'form':form,})

class CatsBuyAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        cats = CatsSerializers(data = request.data)
        # print(dialog.errors)
        if cats.is_valid(): 
            cats.save()
            return Response(status=201)
        else:
            print(cats.errors)
            return Response(status = 400)

class GetUserInfo(APIView):
    def get(self,request):
        user = request.user
        info = Balance.objects.get(user = user)
        serializer = GetUserInfoSerializers(data = info)
        return Response(serializer.data)