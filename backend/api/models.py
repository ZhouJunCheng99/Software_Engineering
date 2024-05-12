from django.db import models
from rest_framework import serializers


class Message(models.Model):
    # subject = models.CharField(max_length=200)
    # body = models.TextField()
    name = models.CharField(max_length=200)
    password = models.TextField()
    # 权限设置,0表示普通用户,1表示管理员
    permission = models.IntegerField(default=0)


class LoginMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'name', 'password', 'permission', 'pk')
