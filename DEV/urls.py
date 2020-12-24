"""DEV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from projects.views import index_page, index_page2, ProjectsCR,ProjectsRUD
# 1、urlpatterns为名称固定的列表，用于存放路由信息
# 2、列表中的元素个数，就是路由条数

# 3、路由配置规则：
# a.从列表的第一个元素开始（从上到下）开始匹配
# b.一旦匹配成功，会自动调用path第二个参数所指定的视图函数
# c.一旦匹配成功之后，不会再往下匹配
# d.如果匹配不成功，会返回一个状态码为404的页面
# e.url路由信息，推荐使用/结尾

# 4、可以在子应用中定义子路由，子应用名/urls.py中来定义
# 5、可以使用include函数来加载子路由，第一个参数为字符串（'子应用名.urls'）
# 6、如果url第一部分匹配成功，那么会将url剩下的部分拿到子路由中去匹配

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('projects.urls')),
    path('projects/', ProjectsCR.as_view()),
    path('projects/<int:pk>/', ProjectsRUD.as_view())
    # path('index/', index_page),
    # path('index2/', index_page2)
]
