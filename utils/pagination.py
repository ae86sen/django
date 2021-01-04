from rest_framework.pagination import PageNumberPagination


# 重写PageNumberPagination类
class MyPagination(PageNumberPagination):
    # 指定默认每页显示数量
    page_size = 2
    # 指定第几页
    page_query_param = 'p'
    # 指定每页显示数量
    page_size_query_param = 's'
    # 指定每页最大显示数量，如果前端指定的数量超出该数量，则显示最大值
    max_page_size = 30
