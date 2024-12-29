
from django.shortcuts import render
from django.http import HttpResponse           ### - библиотека для классов и представлений
from .models import *                          ### - (+++)

# Create your views here. (Создавайте свои мнения здесь.)

### - 19.12.24    ++
### - 29.12.24    +++
### - request - запрос от пользователя
### - "index.html" - указываем шаблон который хотим вернуть


def index_1(request):                     ### - (***)
    Authors = Author.objects.all()
    context = {
        "Authors": Authors,
    }
    return render(request, 'index_1.html', context)

def index_1a(request):                    ### - (***)
    context = {
        "a": "Эта строка через переменую из вьюсов",
    }
    return render(request, 'index_1a.html', context)



def index(request):                                 ### - ++ - обработка логики и возврат шаблона пользователю
    name = request.GET.get('name', "Guest")         ### - Guest - неизвестный пользователь или не авторизованный
    age = request.GET.get('age', "0")
    return HttpResponse(f'Hello, {name} {age}!')


def simple_post(request):                                    ### - ++
    if request.method == "POST":
        message = request.POST.get("message", "")
        return HttpResponse(f"You said: {message}")          ### - You said это надтись перед выводом сообщения
    return render(request, "index2.html")




#___________________________________________________________________________________________________________________
### - 19.12.24 справочная информация

# def index(request):                                     ### - ++ - обработка логики и возврат шаблона пользователю
#     return HttpResponse('Hello', status=400, reason='!!!')  ### - ++
                                    ### - Выводит в консоль данные о запросах пользователей и о каких либо ошибках
#___________________________________________________________________________________________________________________
### - 15.12.24

# class index2(TemplateView):                                ### - класс наследуется от базового шаблона TemplateView
#     template_name = "index2.html"                          ### - Указывается имя нашего шаблона