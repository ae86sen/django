"""
============================
Author:古一
Time:2020/12/20
E-mail:369799130@qq.com
============================
"""
from projects import views
from django.urls import path

urlpatterns = [
    path('projects/', views.ProjectsCR.as_view()),
    path('projects/<int:pk>/', views.ProjectsRUD.as_view())
    # path('projects/', ProjectsCR.as_view())
]
