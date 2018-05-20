#! python3
# -- coding: utf-8

"""mysiteForTranslte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include,path

urlpatterns = [
    path('articleTranlate/', include('articleTranlate.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),            
]
# 函数 include() 允许引用其它 URLconfs。
# 每当 Django 遇到 :func：~django.urls.include 时，
# 它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。


# 我们设计 include() 的理念是使其可以即插即用。
# 因为投票应用有它自己的 URLconf( polls/urls.py )，
# 他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，
# 或者其他任何路径下，这个应用都能够正常工作。

# 当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。