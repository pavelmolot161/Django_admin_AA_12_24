
### - 18.12.24 Именно этот клон работает с репозиторием
### - 13.12.24
### - Эта команда вернет на один уровень выше в адресной строке:
#                                                            >>> cd ..

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                               >>> django.get_version()

### - 4) Создание проекта: - (.venv) PS D:\module_18_Django> >>> django-admin startproject mysite

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                            (.venv) PS D:\module_18_Django> >>> cd mysite
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py startapp app

### - 8) Создание файла зависимостей:
#             (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt
#     8.a) вывод зависимостей в консоль:
#                                                            >>> pip freeze

### - 14.12.24
### - 9) В папке migrations в файле vievs.py создаем функцию:
                                                                # def index(request):
                                                                #     return render(request, "index.html")
### - 10) В папке mysite файле settings.py:
#             в строке TEMPLATES = [] дополняем значение 'DIRS': [] == 'DIRS': [BASE_DIR / "templates"],
#             в строке INSTALLED_APPS = [] в конце дописываем имя нашего приложения 'app'

### - 11) Создание папки templates и файла в ней index.html:
## Определение адреса в этом файле - urban https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami

### - 12) Внесение дополнений в папку mysite файл urls.py:
#                                 from mysite.app.views import index    ### - +
#                                 urlpatterns = [
#                                     path('admin/', admin.site.urls),
#                                     path('', index),                  ### - +
# ]

### - 15.12.24
### - поменял структуру проэкта и убрал вложенность папок проекта mysite, сделал все в ручную перепаскиванием
## соответственно поменялся путь запуска, но в чем была проблема я так и не понял.

### - 13) Внесение дополнений в папку mysite файл urls.py:
#                                 from app.views import index           ### - ++ импорт как в лекции
#                                 urlpatterns = [
#                                     path('admin/', admin.site.urls),
#                                     path('', index),                  ### - +

### - 14) ЗАПУСK НОВЫЙ серверa разработки, (выполнив команду из корневого каталога проекта):
#                     (.venv) PS D:\module_18_Django> >>> python manage.py runserver

### - 15) Создан новый файл HTML в папке templates c названием index2

### - 16) Создание класса в файле views.py папки app - class index2(TemplateView)

### - 17) В файл urls.py папки mysite добален импорт from app.views import index, + index2

### - 16.12.24

### - 18) оформление странички через папку templates файл index.html

### - 19) Внесены дополнения в файл views.py папки app которая связана с файлами html:
                # def index(request):
                #     title = "Заголовок мой сайт (1.a)"
                #     text = 'мой текст (10)'
                #     context = {
                #         'title': title,
                #         'text': text,
                #     }
                #     return render(request, "index.html", context)

### - 17.12.24

### - 20) Создаем папку static
#           a) создаем файл с расщирением css и называем его style.css:
#               - body{
#                   background-color: lightblue;             /* Изменен цвет на светло-голубой это фон сайта*/
#                 }
#                 h1 {
#                   text-align: center;
#                 }

### - 21) Вносим изменения в файл settings.py:
#                                          STATIC_URL = 'static/'
#
#                                          STATICFILES_DIRS = [
#                                             os.path.join(BASE_DIR, 'static'),
#                                          ]
#      Импортируем - import os

### - 22) Дополняем файл views.py функцией base:
#               def base (request):
#                   return render(request, "index2.html")

### - 23) Дополняем файл urls.py:
#               urlpatterns = [
#                   path('admin/', admin.site.urls),
#                   path('', index),
#                   path('base/', base),                   ### - +
#               ]

### - 24) Работа в директории templates:
#               - создание файла i.html:
#                           <p>new text</p>
#               - работа в файлах index.html, index2.html (сохранено ++)

### - 18.12.24 Именно этот клон работает с репозиторием

### - 19.12.24

### - 25) Внесены изменения в папку views:
#                    def index(request):
#                       name = request.GET.get('name', "Guest")
#                       return HttpResponse(f'Hello, {name}!')

### - 26) Работа через адресную строку браузера - Это передача через ГЕТ запрос:
#                   http://127.0.0.1:8000/? >>> http://127.0.0.1:8000/?name=Pavel >>> Enter
#                   http://127.0.0.1:8000/? >>> http://127.0.0.1:8000/?name=Pavel&age=30 >>> Enter


### - 22.12.24 ПРОДОЛЖЕНИЕ В 19 МОДУЛЕ

### - 27) Заполнение папки models.py:

### - 28) ЗАПУСКАЕМ команду, чтобы создать миграции для наших изменений в моделях:
#                       (.venv) PS D:\Rabota_12_24\Django_admin_AA_12_24>  >>> python manage.py makemigrations

### - 29) ПРИМЕНЯЕМ миграции:
#                        (.venv) PS D:\Rabota_12_24\Django_admin_AA_12_24> >>> python manage.py migrate

### - 30) После создания новых моделей создаем миграции к ним:
#                        (.venv) PS D:\Rabota_12_24\Django_admin_AA_12_24>  >>> python manage.py makemigrations

#        вывод к консоль:   Migrations for 'app':
                        #       app\migrations\0003_student_course.py
                        #       + Create model Student
                        #       + Create model Course
                        #   (.venv) PS D:\Rabota_12_24\Django_admin_AA_12_24>

### - 31) опять ПРИМЕНЯЕМ миграции после чего таблици появятся в базе данных:
#                        (.venv) PS D:\Rabota_12_24\Django_admin_AA_12_24> >>> python manage.py migrate

### - 25.12.24

### - КВЕРИ СЕТ ЗАПРОСЫ (QuerySet)

### - 1) Эта команда запускает интерактивную оболочку Python с доступом к Вашему проекту Django:
#                                                      >>> python manage.py shell
### - 2) Импортируем модель для запросов из приложения app:
#                                                      >>> from app.models import Author
### - 3) Извлекает все записи из таблицы, связанной с моделью Author. Он возвращает QuerySet, содержащий всех авторов:
#                                                      >>> Author.objects.all()
### - 4) Запрос на заполнение таблици. в таблице, связанной с моделью Author, будет создана новая запись
# с указанными значениями для полей name и bio:
#                                                      >>> Author.objects.create(name="New Author", bio="test")
### - 5) Узнаем сколько пустых данных в таблице:
#                                                      >>> Author.objects.filter(bio="")

### - 6) Замена данных в таблице, возвращает количество замененных элементов:
#                                                      >>> Author.objects.filter(bio="test2").update(bio="Zamena1")

### - 7) Найти количество объектов в БД, возвращает количество элементов:
#                                                      >>> Author.objects.count()

### - 8) Ищет автора с id=2 в базе данных и сохраняет его в переменной a. Если автора нет, возникает ошибка:
#                                                      >>> a = Author.objects.get(id=2)
#                                                      >>> a                        ### - >>> <Author: Two Author2>
### - 9) УДАЛЕНИЕ объектов в БД:
#                                                      >>> a.delete()

### - 8) Все объекты из базы данных сохраняем в переменной a:
#                                              >>> a = Author.objects.all()
#                                              >>> a   ### - >>> <QuerySet [<Author: New Author>, <Author: Author3>]>

### - 29.12.24

### - 32) Эта команда запускает интерактивную оболочку Python с доступом к Вашему проекту Django:
#                                                      >>> python manage.py shell

### - 33) Импортируем модель для запросов из приложения app:
#                                                      >>> from app.models import Author

### - 34) Извлекает все записи из таблицы, связанной с моделью Author. Он возвращает QuerySet, содержащий всех авторов:
#                                                      >>> Author.objects.all()

### - 35) ВЫХОД из терминала - shell:
#                                                      >>> exit()

### - 36) ЗАПУСK серверa разработки, (выполнив команду из корневого каталога проекта):
#                     (.venv) PS D:\module_18_Django> >>>| python manage.py runserver

### - 37) Создаем несколько объектов в таблице Author:
#                                           >>> python manage.py shell
#                                           >>> from app.models import Author
#                                           >>> Author.objects.create(name="Pavel", bio="Romans")
#                                           >>> Author.objects.create(name="Oleg", bio="Boevik")
#  Обязательно ВЫЙТИ из консоли - shell     >>> exit()















###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

### - Отдельный блок работы с ВЕТКАМИ

# Проверьте текущие ветки с помощью команды:
#                                                    >>> git branch

# Создайте новую ветку для второго домашнего задания:
#                                                    >>> git checkout -b homework_2

# Добавьте и зафиксируйте изменения (ВНИМАНИЕ точка через пробел после add):
#                                                    >>> git add .
#                                                    >>> git commit -m "Добавлено второе домашнее задание"
# Отправьте ветку на удалённый репозиторий:
#                                                    >>> git push origin homework_2

# Переключитесь на ветку, от которой хотите создать новую ветку:
#                                                    >>> git checkout homework_2
# Создайте новую ветку от текущей. Например, если Вы хотите создать ветку для доработки второго задания:
#                                                    >>> git checkout -b homework_2_update
# Внесите изменения в код и зафиксируйте их:
#                                                    >>> git add .
#                                                    >>> git commit -m "Доработка второго домашнего задания"
# Отправьте новую ветку на удалённый репозиторий:
#                                                    >>> git push origin homework_2_update

###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

### - КВЕРИ СЕТ ЗАПРОСЫ (QuerySet)

### - 1) Эта команда запускает интерактивную оболочку Python с доступом к Вашему проекту Django:
#                                                      >>> python manage.py shell
### - 2) Импортируем модель для запросов из приложения app:
#                                                      >>> from app.models import Author
### - 3) Извлекает все записи из таблицы, связанной с моделью Author. Он возвращает QuerySet, содержащий всех авторов:
#                                                      >>> Author.objects.all()
### - 4) Запрос на заполнение таблици. в таблице, связанной с моделью Author, будет создана новая запись
# с указанными значениями для полей name и bio:
#                                                      >>> Author.objects.create(name="New Author", bio="test")
### - 5) Узнаем сколько пустых данных в таблице:
#                                                      >>> Author.objects.filter(bio="")

### - 6) Замена данных в таблице, возвращает количество замененных элементов:
#                                                      >>> Author.objects.filter(bio="test2").update(bio="Zamena1")

### - 7) Найти количество объектов в БД, возвращает количество элементов:
#                                                      >>> Author.objects.count()

### - 8) Ищет автора с id=2 в базе данных и сохраняет его в переменной a. Если автора нет, возникает ошибка:
#                                                      >>> a = Author.objects.get(id=2)
#                                                      >>> a                        ### - >>> <Author: Two Author2>
### - 9) УДАЛЕНИЕ объектов в БД:
#                                                      >>> a.delete()

### - 8) Все объекты из базы данных сохраняем в переменной a:
#                                              >>> a = Author.objects.all()
#                                              >>> a   ### - >>> <QuerySet [<Author: New Author>, <Author: Author3>]>

### - 9) ВЫХОД из терминала - shell:
#                                                      >>> exit()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





##############################################################################################################
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

############################################################################################################

### - index.html 17.12.24

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
# </head>
# <body>
#     <h1>{{ text }}</h1>
#     <h1>{{ name }}</h1>
#     {% for i in list %}
#         <p>{{ i|upper }}</p>
#         <p>{{ i|title }}</p>
#     {% endfor %}
#     {% for i in list1 %}
#         <p>{{ i }}</p>
#         <p>{{ i|floatformat:3 }}</p>
#     {% endfor %}
#     {% if len_list > 3 %}
#         <h2>Ok</h2>
#     {% else %}
#         <h2>Not Ok</h2>
#     {% endif %}
#
#
# </body>
# </html>

#_____________________________________________________________________________________________________________

### - index.html (++)

# <!DOCTYPE html>
#
# <html lang="en">
# {% load static %}
# <head>
#     <meta charset="UTF-8">
#     <title>{% block title %}My Site{% endblock %}</title>
#     <link rel = 'stylesheet' type="text/css" href="{% static 'style.css' %}">
# </head>
#
# <head>
# <body>
#     <header>
#         {% block header %}
#         <h1>Welcome to My Site 1</h1>
#         {% endblock %}
#     </header>
#
#     <nav>
#         {% block navigation %}
#         <ul>
#             <li><a href='/'>Home</a></li>
#             <li><a href='/about/'>About</a></li>
#             <li><a href='/contact/'>Contact</a></li>
#         </ul>
#         {% endblock %}
#     </nav>
#
#     <main>
#         {% block content %}
#             <p>Тут будут посты</p>            <!--Коментарий-->
#         {% endblock %}
#     </main>
#
#     <footer>
#         {% block footer %}
#             <p>2023 My Site</p>
#         {% endblock %}
#     </footer>
# </body>
# </html>
#

################################################################################################################

### - index2.html

# {% extends 'index.html' %}
#
# {% block title %}Home - {{ block.super }}{% endblock %}
# <!---->
# {% block header %}
#     {{ block.super }}
#     <h2>{{ Welcome to the 2 Page }}</h2>
# {% endblock %}
#
# {% block content %}
#     <h2>{{ Latest Posts }}</h2>
#     <ul>
#         <li>Post 1</li>              <!--Коментарий-->
#         <li>Post 2</li>
#         <li>Post 3</li>
#     </ul>
# {% endblock %}                       <!--Коментарий-->
#
# {% block footer %}
#     <p>{{ Latest Posts }}</p>
#     {{ block.super }}
# {% endblock %}
#
#
# <!--Коментарий-->
#
#__________________________________________________________________________________________________

### - index2.html    (++)

# {% extends 'index.html' %}                                       <!--Указывает от какого шаблона будет наследоватся-->
#
# {% block title %}Home - {{ block.super }}{% endblock %}
# <!---->
# {% block header %}
#     {{ block.super }}                                            <!--Прийдет инфа из другого блока по наследованию-->
#     <h2>Welcome to the 2 Page</h2>
# {% endblock %}
#
# {% block content %}
#     <h2>Latest Posts </h2>
#     <ul>
#         <li>Post 1</li>           <!--Коментарий-->
#         <li>Post 2</li>
#         <li>Post 3</li>
#     </ul>
# {% endblock %}                       <!--Коментарий-->
#
# {% block footer %}
#     <p>Thanks for visiting</p>
#     {{ block.super }}
# {% endblock %}

####################################################################################################################

### index.html 19.12.23
#
# <!DOCTYPE html>
#
# <html lang="en">
# {% load static %}                                        <!--Импорт static или загрузка функции проверка-->
# <head>
#     <meta charset="UTF-8">
#     <title>{% block title %}My Site{% endblock %}</title>
#     <link rel = 'stylesheet' type="text/css" href="{% static 'style.css' %}">
# </head>
#
# <head>
# <body>
#     <header>
#         {% block header %}
#         <h1>Welcome to My Site 1</h1>
#         {% endblock %}
#     </header>
#
#     <nav>
#         {% block navigation %}
#         <ul>
#             <li><a href='/'>Home</a></li>
#             <li><a href='/about/'>About</a></li>
#             <li><a href='/contact/'>Contact</a></li>
#         </ul>
#         {% endblock %}
#     </nav>
#
#     <main>
#         {% block content %}
#             <p>Тут будут посты</p>                                          <!--Коментарий-->
#         {% endblock %}
#     </main>
#
#     <footer>
#         {% block footer %}
#             <p>2023 My Site</p>
#         {% endblock %}
#     </footer>
# </body>
# </html>

####################################################################################################################

### - index2.html 19.12.24

# {% extends 'index.html' %}          <!-- extends Указывает от какого шаблона будет наследоватся, или кто родительский класс-->
#
# {% block title %}Home - {{ block.super }}{% endblock %}
# <!---->
# {% block header %}
#     {{ block.super }}                                            <!--Прийдет инфа из другого блока по наследованию-->
#     <h2>Welcome to the 2 Page</h2>
# {% endblock %}
#
# {% block content %}
#     <h2> Latest Posts </h2>
#     <ul>
#         <li>Post 1</li>               <!--Коментарий проверка-->
#         <li>Post 2</li>
#         <li>Post 3</li>
#     </ul>
# {% endblock %}                        <!--Закрытие блока проверка-->
#
# {% block footer %}
#     <p>Thanks for visiting</p>
#     {{ block.super }}                                      <!--Переносит инфу из блока footer родительского класса-->
# {% endblock %}
#
