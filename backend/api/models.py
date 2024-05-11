from django.db import models
from rest_framework import serializers


class Message(models.Model):
    # subject = models.CharField(max_length=200)
    # body = models.TextField()
    name = models.CharField(max_length=200)
    password = models.TextField()


class LoginMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'name', 'password', 'pk')
