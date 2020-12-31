from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.getTrafficList.as_view(), name='index'),
    path('statistics/', views.statistics, name='statistics'),
    path('infomation/', views.infomation, name='infomation'),
    path('getConzoneCode/', views.getConzoneCode, name='getConzoneCode'),
    path('getUpDownCode/', views.getUpDownCode, name='getUpDownCode')
]