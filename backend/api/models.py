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



class Water_Quality_Data(models.Model):
    # 监测时间，如果监测时间是日期类型，使用DateTimeField
    # monitoring_time = models.DateTimeField()
    monitoring_time = models.CharField(max_length=30, null=True)
    # 水质类别，例如：Ⅰ、Ⅱ、Ⅲ等，使用CharField存储分类字符串
    water_quality_category = models.CharField(max_length=10, null=True)
    # 水温，使用FloatField存储浮点数
    water_temperature = models.FloatField(null=True)
    # pH值，使用FloatField存储浮点数
    pH = models.FloatField(null=True)
    # 溶氧量，单位为mg/L，使用FloatField存储
    dissolved_oxygen = models.FloatField(null=True)
    # 电导率，单位为μS/cm，使用FloatField存储
    conductivity = models.FloatField(null=True)
    # 浊度，单位为NTU，使用FloatField存储
    turbidity = models.FloatField(null=True)
    # 高锰酸盐指数，单位为mg/L，使用FloatField存储
    permanganate_index = models.FloatField(null=True)
    # 氨氮，单位为mg/L，使用FloatField存储
    ammonia_nitrogen = models.FloatField(null=True)
    # 总磷，单位为mg/L，使用FloatField存储
    total_phosphorus = models.FloatField(null=True)
    # 总氮，单位为mg/L，使用FloatField存储
    total_nitrogen = models.FloatField(null=True)
    # 站点情况，例如：正常、维护等，使用CharField存储
    site_status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.monitoring_time} - {self.water_quality_category} - {self.water_temperature} - {self.site_status}"

class WaterQualityDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Water_Quality_Data
        fields = ('url', 'monitoring_time', 'water_quality_category', 'water_temperature', 'pH',
                  'dissolved_oxygen', 'conductivity', 'turbidity', 'permanganate_index',
                  'ammonia_nitrogen', 'total_phosphorus', 'total_nitrogen', 'site_status', 'pk')