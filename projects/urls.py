"""
============================
Author:古一
Time:2020/12/20
E-mail:369799130@qq.com
============================
"""
from projects.views import index_page, index_page2
from django.urls import path

urlpatterns = [
    path('index/', index_page),
    path('index2/', index_page2)
]