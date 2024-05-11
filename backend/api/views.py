from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import action

from .models import Message, LoginMessageSerializer


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

        login_message = Message.objects.filter(name=name, password=password)

        if login_message:
            return JsonResponse({'result': True})
        else:
            return JsonResponse({'result': False})


