import json
import random

from faker import Faker
from django.http import HttpResponse, JsonResponse
from django.views import View

from interfaces.models import Interfaces
from projects.models import Projects
from django.db import connection

from projects.serializers import ProjectsSerializer,ProjectsModelSerializer


def index_page(request):
    if request.method == 'GET':
        return HttpResponse("<h2>GET请求：hello,jack!</h2>")
    elif request.method == 'POST':
        return HttpResponse("<h2>POST请求：hello,jack!</h2>")
    elif request.method == 'PUT':
        return HttpResponse("<h2>PUT请求：hello,jack!</h2>")
    elif request.method == 'DELETE':
        return HttpResponse("<h2>DELETE请求：hello,jack!</h2>")


def index_page2(request):
    return HttpResponse("<h2>hello,jack222!</h2>")


class IndexPage(View):
    """
    类视图
    1、必须要继承View
    2、可以定义get,post,put,delete方法，来实现GET，POST,PUT,DELETE请求
    3、get,post,put,delete方法名称固定且均为小写
    4、实例方法的第二个参数为HttpRequest对象或其子类对象
    5、一定要返回一个HttpResponse对象
    """

    def get(self, request, page_id):
        # 5、url后面的？号参数，成为query string查询字符串参数
        # 6、request.GET去获取参数字符串参数
        # 7、request.GET返回QueryDict对象，类似于一个字典，支持字典中的所有操作
        # 8、request.GET[key]、request.GET.get[key]、request.GET.getlist()去获取参数值
        faker = Faker(locale='zh_CN')
        for i in range(20):
            name = faker.name()
            print(name)
            temp_dict = {
                "name": name,
                "tester": f"xxx测试0{i}",
                "desc": "xxx描述",
                "projects_id": random.choice([1, 2, 5, 6])
            }
            temp_obj = Interfaces.objects.create(**temp_dict)
        return JsonResponse("<h2>GET请求：hello,jack!</h2>")

    def post(self, request, page_id):
        # 一、创建（C）
        # 1、使用模型类对象来创建
        # 会创建一个Projects模型类对象，但是还未提交
        project_obj = Projects(name='共享单车项目', leader='xxx项目负责人4',
                               tester='xxx测试5', programmer='xxx研发6')
        # 需要调用模型对象的save()方法，去提交
        project_obj.save()
        # 2、可以使用查询集的create方法
        # objects是manager对象，用于对数据进行操作
        # 使用模型类.objects.create()方法，无需调用save方法
        # project_obj = Projects.objects.create(name='xxx项目5', leader='xxx项目负责人5',
        #                                       tester='xxx测试5', programmer='xxx研发5')

        # 二、更新（U）
        # 1、先获取模型类对象，然后修改某些字段，再调用save方法保存
        # project_obj = Projects.objects.get(id=1)
        # project_obj.name = '阿里云项目'
        # project_obj.save()

        # 2、可以使用模型类名.objects.filter(字段名=值).update(字段名=修改的值)
        # one = Projects.objects.filter(id=2).update(name='腾讯云项目')

        # 三、删除（D）
        # 1、使用模型对象.delete()
        # project_obj = Projects.objects.get(id=4)
        # one = project_obj.delete()

        # 四、查询（C）
        # 使用objects管理器来查询
        # 1、get方法
        # a.一般只能使用主键或者唯一键作为查询条件
        # b.get方法如果查询的记录为空和多条记录，那么会抛出异常
        # c.返回的模型类对象，会自动提交
        # one = Projects.objects.get(id=1)
        # qs = Projects.objects.all()
        data = json.loads(request.body, encoding='utf-8')
        return HttpResponse(f"<h2>POST请求：hello,{data['name']}!</h2>")

    def put(self, request, page_id):
        # a、HttpResponse对象，第一个参数为字符串类型或字节类型，会将字符串内容返回给前端
        # b、可以使用content_type来指定内容类型
        # c、可以使用status参数来指定响应状态码
        return HttpResponse("<h2>PUT请求：hello,jack!</h2>")

    def delete(self, request, page_id):
        return HttpResponse("<h2>DELETE请求：hello,jack!</h2>")




class ProjectsCR(View):

    def get(self, request):
        """查询所有项目"""
        # 1、从数据库中获取所有的项目信息（查询集）
        qs = Projects.objects.all()
        # 2、将模型类对象（查询集）转化为嵌套字典的列表
        # 1.可以使用序列化器类来进行序列化输出
        # a.instance参数可以传模型类对象
        # b.instance参数可以传查询集（多条记录），many=True
        # c.可以ProjectsSerializer序列化器对象，调用data属性，可以将模型类对象转化为Python中的数据类型
        # d.如果未传递many=True参数，那么序列化器对象.data，返回字典，否则返回一个嵌套字典的列表
        serializer_obj = ProjectsModelSerializer(instance=qs, many=True)

        return JsonResponse(serializer_obj.data, safe=False)

    def post(self, request):
        """添加项目"""
        ret = {
            "msg": "",
            "code": 0
        }
        # 1、获取从前端传来的项目信息并转化为python中数据类型（字典或者嵌套字典的列表）
        # 第一层校验，校验是否为json格式数据
        try:
            python_data = json.loads(request.body, encoding='utf-8')
        except Exception as e:
            result = {
                "msg": "参数有误，需要json格式数据",
                "code": 0
            }
            return JsonResponse(result, status=400)
        # 2、校验字段
        # 第二层校验，校验字段是否合法
        serializer_obj = ProjectsModelSerializer(data=python_data)
        try:
            serializer_obj.is_valid(raise_exception=True)
        except Exception:
            ret['msg'] = '参数错误'
            ret.update(serializer_obj.errors)
            return JsonResponse(ret, status=400)
        # 3、校验通过则创建项目
        serializer_obj.save()
        # 4、向前端返回json格式数据
        ret['msg'] = '创建成功'
        ret.update(serializer_obj.data)
        return JsonResponse(ret)


class ProjectsRUD(View):

    def get_object(self,pk):
        try:
            obj = Projects.objects.get(id=pk)
        except Exception as e:
            result = {
                "msg": "参数有误",
                "code": 0
            }
            return JsonResponse(result, status=400)
        return obj

    def get(self, request, pk):
        """查询项目详情"""
        # 1、校验pk参数是否合法
        obj = self.get_object(pk)
        # 2、将查询集对象转化为python类型：字典
        serializer_obj = ProjectsModelSerializer(instance=obj)
        # 3、将字典输出到前端
        return JsonResponse(serializer_obj.data)

    def put(self, request, pk):
        """修改项目信息"""
        ret = {
            "msg": "",
            "code": 0
        }
        # a.校验pk值并获取待更新的模型类对象
        obj = self.get_object(pk)
        # b.校验前端所传的json数据是否合法
        try:
            python_data = json.loads(request.body)
        except Exception:
            result = {
                "msg": "参数有误，需要json格式数据",
                "code": 0
            }
            return JsonResponse(result, status=400)
        # c.更新操作
        # 如果在定义序列化器对象时，同时指定instance和data参数
        # a.调用序列化器对象.save()方法，会自动调用序列化器类中的update方法
        serializer_obj = ProjectsModelSerializer(instance=obj, data=python_data)
        try:
            serializer_obj.is_valid(raise_exception=True)
        except Exception:
            ret['msg'] = '参数有误'
            ret.update(serializer_obj.errors)
            return JsonResponse(ret, status=400)
        serializer_obj.save()
        # d.向前端返回json格式的数据
        return JsonResponse(serializer_obj.data, status=201)

    def delete(self, request, pk):
        """删除项目"""
        # a.校验pk值并获取待删除的模型类对象
        obj = self.get_object(pk)

        obj.delete()

        python_data = {
            'msg': '删除成功',
            'code': 1
        }
        return JsonResponse(python_data, status=200)
