from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 首页
    path('page1/', views.page1, name='page1'),  # 第一个页面
    path('page2/', views.page2, name='page2'),  # 第二个页面
    path('page3/', views.page3, name='page3'),  # 第三个页面
]