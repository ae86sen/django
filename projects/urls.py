"""
============================
Author:古一
Time:2020/12/20
E-mail:369799130@qq.com
============================
"""
from projects.views import index_page, index_page2, IndexPage
from django.urls import path

urlpatterns = [
    path('index/', index_page),
    path('index2/', index_page2),
    # 类视图定义路由
    # 1、path的第二个参数为类名.as_view()
    # 2、可以使用<url类型转化器:路径参数名>
    # 3、类型包括int、path、uuid、slug等
    path('index3/<int:page_id>', IndexPage.as_view())
]