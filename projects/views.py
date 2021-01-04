import json
import random

from faker import Faker
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from interfaces.models import Interfaces
from projects.models import Projects
from django.db import connection
from interfaces.serializers import InterfacesModelSerializer
from projects.serializers import ProjectsSerializer, ProjectsModelSerializer


# class ProjectsCR(generics.ListCreateAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsModelSerializer
#     # filter_backends = [DjangoFilterBackend, OrderingFilter]
#     ordering_fields = ["id", "name"]
#     # 需要过滤哪些就写哪些，名字必须与模型类中字段一致
#     filterset_fields = ["name", "id"]
#
#
# class ProjectsRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsModelSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "name"]
    # 需要过滤哪些就写哪些，名字必须与模型类中字段一致
    filterset_fields = ["name", "id"]
