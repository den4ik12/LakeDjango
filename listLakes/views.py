from django.shortcuts import render

from listLakes.models import Lake


# Контроллер для главной страницы
def home(request):
    title = "Главная"
    return render(request, "index.html", {"title": title})


# Контроллер для списка озер
def listLakes(request):
    title = "Список озер"
    # Получение списка из бд
    listLake = Lake.objects.all()
    return render(request, "listLakes.html", {"title": title, "listLake": listLake})
