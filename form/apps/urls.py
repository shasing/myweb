"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apps.views import home,abc,gmail,indexs,base,new_user,login,relogin

urlpatterns = [
    path('home/', home , name="home"),
    path('abc/', abc , name="abc"),
    path('indexs/', indexs, name="indexs"),
    path('gmail/', gmail, name="gmail"),
    path('base/', base, name="base"),
    path('new_user/', new_user, name="new_user"),
    path('login/', login, name="login"),
    path('relogin/', relogin, name="relogin")
  ]

   



 