"""viber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include

from .views import ViberUserView, callback, set_webhook, unset_webhook, send_message_for_user, ViberUserListView, ViberUserCreate


urlpatterns = [
    path('callback/', callback),# в URL указываем путь, это hi/(localhost:8000/hi) далее указываем на .py файл(views) и через точку указываем на имя функции в этом файле (views)
    path('set_webhook/', set_webhook),
    path('unset_webhook/', unset_webhook),
    path('send_message/', send_message_for_user),
    path('hi/', ViberUserView.as_view()),
    path('all/', ViberUserListView.as_view(), name='users_all'),
    path('user/add', ViberUserCreate.as_view()),
]
