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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from interfaces.models import Interfaces
from projects.models import Projects
from django.db import connection
from interfaces.serializers import InterfacesModelSerializer
from projects.serializers import ProjectsSerializer, ProjectsModelSerializer


class XMixin:
    def list(self, request):
        qs = self.filter_queryset(self.get_queryset())
        # 对查询结果进行分页查询，返回结果依然是个查询集对象，有可能为空
        page = self.paginate_queryset(qs)
        # 如果不为空，则进行分页
        if page is not None:
            # 获取序列化对象
            serializer_obj = self.get_serializer(instance=page, many=True)
            # 返回分页查询结果
            return self.get_paginated_response(serializer_obj.data)
        serializer_obj = self.get_serializer(instance=qs, many=True)
        return Response(serializer_obj.data, status=status.HTTP_200_OK)


class ProjectsCR(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "name"]
    # 需要过滤哪些就写哪些，名字必须与模型类中字段一致
    filterset_fields = ["name", "id"]

    def get(self, request, *args, **kwargs):
        """查询所有项目"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """添加项目"""
        return self.create(request, *args, **kwargs)


class ProjectsRUD(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer

    def get(self, request, *args, **kwargs):
        """查询项目详情"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """修改项目信息"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """删除项目"""
        return self.destroy(request, *args, **kwargs)
