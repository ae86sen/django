import json
import random

from faker import Faker
from django.http import HttpResponse
from django.views import View

from interfaces.models import Interfaces
from projects.models import Projects
from django.db import connection


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
        return HttpResponse("<h2>GET请求：hello,jack!</h2>")

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
