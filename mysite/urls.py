"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

### - 14.12.24
### - 15.12.24
### - 17.12.24    +
### - 19.12.24    +++
### - 29.12.24    ++++
from app.views import index, simple_post   ### - +++
from app.views import index
from app.views import index_1, index_1a    ### - ++++

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_1),
    path('index_1a/', index_1a)
]






### - Справочно_____________________________________________________________________________________________
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('index/', simple_post),           ### - +++
#
#     # path('index/', index2.as_view()),               ### - ++.a  as_view() - Стандарт запуска из класса
#     # path('base/', base),                            ### - +
# ]
