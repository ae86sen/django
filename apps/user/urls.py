from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
]
