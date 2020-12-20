from django.http import HttpResponse


def index_page(request):
    return HttpResponse("<h2>hello,jack!</h2>")


def index_page2(request):
    return HttpResponse("<h2>hello,jack222!</h2>")
