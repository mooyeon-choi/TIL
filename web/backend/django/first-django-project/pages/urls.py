from django.urls import path
# 같은 디렉토리에 있는 views를 가져옴
from . import views

urlpatterns = [
    # 1. url 설정
    # path(url, 해당하는 views의 함수)
    path('', views.index),
    # variable routing
    # url의 특정값을 변수처럼 활용
    path('hello/<str:name>/', views.hello),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('cube/<int:number>/', views.cube),
    path('about/<str:name>/<int:age>/', views.about),
    path('info/', views.info),
    path('isitgwangbok/', views.isitgwangbok),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('signup/', views.signup),
    path('signup_result/', views.signup_result),
]