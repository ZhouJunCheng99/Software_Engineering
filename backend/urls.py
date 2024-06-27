"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .api.views import index_view, LoginMessageViewSet, GetHistoryData, WaterQualityDataViewSet, ExportDataViewSet

# 确保每个视图集都有唯一的 basename !!!
# basename 参数用于为视图集提供一个唯一的名称，这个名称在整个应用中必须是唯一的。如果你没有显式地设置 basename，
# Django Rest Framework 会使用视图集的类名作为 basename，并且可能会导致重复。
router = routers.DefaultRouter()
router.register('account', LoginMessageViewSet)
router.register('water-data', WaterQualityDataViewSet, basename='water_quality_data')

# info-history_data
router.register('history_data', GetHistoryData, basename='history_data')

# router.register('upload_water_quality', WaterQualityDataViewSet)
router.register('export', ExportDataViewSet, basename='export_data')




urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]


