import json

from django.http import HttpResponse
from django.views import View


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

    def get(self,request,page_id):
        # 5、url后面的？号参数，成为query string查询字符串参数
        # 6、request.GET去获取参数字符串参数
        # 7、request.GET返回QueryDict对象，类似于一个字典，支持字典中的所有操作
        # 8、request.GET[key]、request.GET.get[key]、request.GET.getlist()去获取参数值
        return HttpResponse("<h2>GET请求：hello,jack!</h2>")

    def post(self,request,page_id):
        # a、可以使用request.POST方法，去获取application/x-www-urldecoded
        # b、可以使用request.body方法，去获取application/json类型的参数
        # c、可以使用request.META方法（或request.headers方法），去获取请求头参数，key为HTTP_请求头key的大写
        data = json.loads(request.body,encoding='utf-8')
        return HttpResponse(f"<h2>POST请求：hello,{data['name']}!</h2>")

    def put(self,request,page_id):
        # a、HttpResponse对象，第一个参数为字符串类型或字节类型，会将字符串内容返回给前端
        # b、可以使用content_type来指定内容类型
        # c、可以使用status参数来指定响应状态码
        return HttpResponse("<h2>PUT请求：hello,jack!</h2>")

    def delete(self,request,page_id):
        return HttpResponse("<h2>DELETE请求：hello,jack!</h2>")