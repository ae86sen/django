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
    path('index/', views.index_page),
    path('index2/', views.index_page2),
    # 类视图定义路由
    # 1、path的第二个参数为类名.as_view()
    # 2、可以使用<url类型转化器:路径参数名>
    # 3、类型包括int、path、uuid、slug等
    path('index3/<int:page_id>', views.IndexPage.as_view()),
    path('projects/', views.ProjectsCR.as_view()),
    path('projects/<int:pk>/', views.ProjectsRUD.as_view())
    # path('projects/', ProjectsCR.as_view())
]
