from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import TaskSerializer
from .models import Task

# csrf_exampt означает, что токен не нужен, а если csrf_promt, то нужен
@csrf_exempt
def task (request):
    if request.method == "GET":
# в all_data мы записываем все данные из модели в переменную
        all_data = Task.objects.all()
# мы передаём данные в сериализатор, что бы получить JSON
        serializer_class = TaskSerializer(all_data,many = True)
# return отдаёт ответ пользователю в виде JSON
        return JsonResponse(serializer_class.data, safe = False)
        # return render(request,"api.html",{"key_a":serializer_class.data})
    elif request.method == "POST":
# преобразуем наши данные из JSON
        data = JSONParser().parse(request)
# отправляем данные в сериализатор
        serializer_class = TaskSerializer(data = data)
# проверяем правильно ли эти данные заполнены
        if serializer_class.is_valid():
# сохраняем
            serializer_class.save()
# отдаём ответ со статусом 201
            return JsonResponse(serializer_class.data, status = 201)
# иначе ошибка
        return JsonResponse(serializer_class.errors, status = 400)


@csrf_exempt
def task_detale (request, pk):
    try: # проверка
        task = Task.objects.get(pk = pk) # Get это получемие определённой записи
    except: # если ошибка
        #return HttpResponse(status = 404)
        return render(request, "erors.html", status = 404)

    if request.method == "GET":
# сериализуем запись что бы получить JSON
        serializer_class = TaskSerializer(task,many = False)
        return JsonResponse(serializer_class.data, safe = False)

    elif request.method == "PUT":
# преобразуем наши данные из JSON
        data = JSONParser().parse(request)
# отправляем данные в сериализатор, указываем запись, если всё правильно - обновляем
        serializer_class = TaskSerializer(task,data = data)
# проверяем правильно ли эти данные заполнены
        if serializer_class.is_valid():
# сохраняем
            serializer_class.save()
# отдаём ответ со статусом 201
            return JsonResponse(serializer_class.data, status = 201)
# иначе ошибка
        return JsonResponse(serializer_class.errors, status = 400)

    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"massage": "deleted"}, status = 204)


