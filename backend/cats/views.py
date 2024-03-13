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
        cats = AboutCats.objects.filter(user = request.user).count()
        print(cats)
        if cats > 0 and request.user and request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        cats = AboutCats.objects.filter(user = request.user).count()
        print(cats)
        if cats > 0:
            return True
        return False


class CatsAPI(APIView):
    permission_classes = [CatsPermission]

    def get(self,request):
        cats = AboutCats.objects.filter(user = request.user)
        # cats = AboutCats.objects.all()
        print(cats)
        serializers = CatsSerializers(cats, many = True)
        # print(serializers.data)
        return Response({'data':serializers.data})
    
    def post(self,request):
        cats = CatsSerializers(data = request.data) #передаём основные данные 
        # print(dialog.errors)
        print(request.data)
        if cats.is_valid(): 

            cats.save(user = request.user) # сохраняем запись с сохранением пользователя
            return Response(status=201)
        else:
            print(cats.errors)
            return Response(status = 400)
    

class CatsBuyAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        id_cat = request.POST.get("id_cat")
        print(request.POST)
        id_buyer =request.user
        # делаем запрос к БД
        cat = AboutCats.objects.get(id = int(id_cat))

        if cat is None: return Response(status = 400)
        cost = cat.cost
        buyer = Balance.objects.get(user = id_buyer)
        if buyer is None: return Response(status = 400)
        balance_buyer = buyer.balance
        if balance_buyer < cost: return Response(status = 400)
        seller = Balance.objects.get(user = cat.user)

        buyer.balance -= cost
        seller.balance += cost
        cat.user = id_buyer
        
        CatHistory.objects.create(seller = seller, buyer = buyer, cat = cat, cost = cost)

        buyer.save()
        seller.save()
        cat.save()
        return Response({'message':"продано"}, status = 200)

        # cats = CatsSerializers(data = request.data)
        # # print(dialog.errors)
        # if cats.is_valid(): 
        #     cats.save()
        #     return Response(status=201)
        # else:
        #     print(cats.errors)
        #     return Response(status = 400)

class GetUserInfo(APIView):
    def get(self,request):
        user = request.user
        info = Balance.objects.get(user = user)
        serializer = GetUserInfoSerializers(info, many = False)
        return Response(serializer.data)

class UserHistoryAPI(APIView):
    def get(self,request):
        cats = CatHistory.objects.filter(Q(buyer = request.user) | Q(seller = request.user))
        # cats = AboutCats.objects.all()
        print(cats)
        serializers = CatHistorySerializers(cats, many = True)
        # print(serializers.data)
        return Response({'data':serializers.data})
        
        
######################################################################  функции Django

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

class CatShopAPI(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        # cats = AboutCats.objects.filter(user = request.user)
        cats = AboutCats.objects.all().exclude(user = request.user)
        print(cats)
        serializers = CatsSerializers(cats, many = True)
        # print(serializers.data)
        return Response({'data':serializers.data})
