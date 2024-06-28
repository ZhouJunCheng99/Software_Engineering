from django.db import models
from rest_framework import serializers


class Message(models.Model):
    # subject = models.CharField(max_length=200)
    # body = models.TextField()
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, default="123456789")
    password = models.TextField()
    # 权限设置,0表示普通用户(养殖户) ,1表示管理员, 2表示食品购买者
    permission = models.IntegerField(default=0)

class LoginMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'name', 'phone_number', 'password', 'permission', 'pk')



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


# 鱼类数据模型
# 编号	品种	体长(cm)	体重(kg)	健康状况	鱼群状况	繁殖期	鱼群总量(t)	鱼苗数量	成鱼数量
class Fish_Data(models.Model):
    # 编号
    id = models.AutoField(primary_key=True)
    # 品种
    species = models.CharField(max_length=50, null=True)
    # 体长
    body_length = models.FloatField(null=True)
    # 体重
    body_weight = models.FloatField(null=True)
    # 健康状况
    health_status = models.CharField(max_length=20, null=True)
    # 鱼群状况
    fish_group_status = models.CharField(max_length=20, null=True)
    # 繁殖期
    breeding_period = models.CharField(max_length=20, null=True)
    # 鱼群总量
    fish_group_total = models.FloatField(null=True)
    # 鱼苗数量
    fry_number = models.FloatField(null=True)
    # 成鱼数量
    adult_fish_number = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id} - {self.species} - {self.body_length} - {self.body_weight} - {self.health_status} - {self.fish_group_status} - {self.breeding_period} - {self.fish_group_total} - {self.fry_number} - {self.adult_fish_number}"

class FishDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fish_Data
        fields = ('url', 'species', 'body_length', 'body_weight', 'health_status',
                  'fish_group_status', 'breeding_period', 'fish_group_total',
                  'fry_number', 'adult_fish_number', 'pk')