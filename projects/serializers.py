"""
============================
Author:古一
Time:2020/12/25
E-mail:369799130@qq.com
============================
"""
from rest_framework import serializers

from projects.models import Projects
from interfaces.models import Interfaces
from interfaces.serializers import InterfacesModelSerializer


class ProjectsSerializer(serializers.Serializer):
    """
    可以定义序列化器类，来实现序列化和反序列化操作
    a.一定要继承serializers.Serializer或者Serializer的子类
    b.默认情况下，可以定义序列化器字段，序列化器字段名要与模型类中字段名相同
    c.默认情况下，定义几个序列化器字段，那么就会返回几个数据（到前端，序列化输出的过程），前端也必须得传递这几个字段（反序列化过程）
    """
    name = serializers.CharField(max_length=10, label='项目名称', help_text='项目名称', min_length=2)
    # 如果一个字段设置了read_only=True，那么该字段前端可以不用传入该字段，但是响应结果会返回该字段
    leader = serializers.CharField(max_length=200, label='项目负责人', help_text='项目负责人')
    tester = serializers.CharField(max_length=200, label='测试人员', help_text='测试人员', write_only=True)
    # 如果一个字段设置了write_only=True，那么该字段将不会返回，但是，如果返回结果serializer_obj.validated_data,那么依然会返回
    programmer = serializers.CharField(max_length=200, label='开发人员', help_text='开发人员', read_only=True)


class ProjectsModelSerializer(serializers.ModelSerializer):
    # 父表获取字表信息
    # a.默认可以使用子表模型类名小写_set
    # interfaces_set = InterfacesModelSerializer(label='所拥有的接口', many=True)
    # b.如果某个字段返回的结果有多条，那么需要添加many=True参数
    # c.如果模型类中外键字段定义了related_name参数，那么会使用这个名称作为字段名
    # interfaces_set = serializers.StringRelatedField(many=True)
    # interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ('desc', 'create_time', 'update_time')
        read_only_fields = ('id', 'desc')
        # 可以在extra_kwargs属性中，来定制某些字段
        extra_kwargs = {
            'programmer': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        # email = validated_data.pop('email')
        return super().create(validated_data)


class ProjectsNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class InterfacesByProjectIdModelSerializer(serializers.ModelSerializer):
    interfaces = InterfacesNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('interfaces',)
