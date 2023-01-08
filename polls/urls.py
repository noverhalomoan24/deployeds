from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='polls'),
    path('dasar-analisis-data',views.analisis_data,name='analisis_data')
]