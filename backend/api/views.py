from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import action

from .models import Message, LoginMessageSerializer
from .models import Water_Quality_Data, WaterQualityDataSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class LoginMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = LoginMessageSerializer

    # 获取前端post的payload传来的name和password,查询数据库中是否存在
    @action(detail=False, methods=[ 'post'])
    def query(self, request):
        # subject = request.GET.get('subject')
        #
        # body = request.GET.get('body')
        name = request.data['name']
        password = request.data['password']
        # 打印收到的数据
        # print(subject)
        # print(body)

        # login_message = Message.objects.filter(name=name, password=password)
        # 这里先取第一个,因为注册还没有设置不能重复
        login_message = Message.objects.filter(name=name, password=password).first()

        # 注意需要先检查 login_message 是否包含任何 Message 实例!!!
        # 如果 QuerySet 为空，first() 方法将返回 None
        if login_message is None:
            return JsonResponse({'result': False})
        elif login_message.permission == 0:
            return JsonResponse({'result': "user"})
        elif login_message.permission == 1:
            return JsonResponse({'result': "admin"})
        else:
            return JsonResponse({'result': False})



class WaterQualityDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows water quality data to be viewed or edited.
    """
    queryset = Water_Quality_Data.objects.all()
    serializer_class = WaterQualityDataSerializer