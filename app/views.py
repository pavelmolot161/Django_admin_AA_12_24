
from django.shortcuts import render

# Create your views here. (Создавайте свои мнения здесь.)

### - 16.12.24
### - 17.12.24    +
### - requestrequest - запрос от пользователя
### - "index.html" - указываем шаблон который хотим вернуть
def index(request):                                        ### - обработка логики и возврат шаблона пользователю
    text = 1
    name = 'tom'
    list = ['aa', 'bb', 'cc']
    list1 = [1.1, 2.2, 3.3, 4.4]
    len_list = len(list1)
    context = {
        'text':text,
        "name": name,
        "list":list,
        "list1":list1,
        "len_list":len_list
    }

    return render(request, "index.html", context)

def base (request):
    return render(request, "index2.html")       ### - +

### - 15.12.24

# class index2(TemplateView):                                ### - класс наследуется от базового шаблона TemplateView
#     template_name = "index2.html"                          ### - Указывается имя нашего шаблона