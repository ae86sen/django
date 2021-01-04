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
    path('projects/', views.ProjectsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('projects/<int:pk>/', views.ProjectsViewSet.as_view({'get': 'retrieve',
                                                              'put': 'update', 'delete': 'destroy'}))
    # path('projects/', ProjectsCR.as_view())
]
