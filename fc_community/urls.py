"""fc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from fcuser.views import home

urlpatterns = [
    # admin 하위에 있는 url은 admin.site.urls 안에서 연결
    path('admin/', admin.site.urls),
    # fcuser 하위에 있는 url은 fcuser.urls 안에서 연결
    path('fcuser/', include('fcuser.urls')),
    path("", home),  # 홈 url은 home 함수 호출
    path("board/", include("board.urls"))
]
