from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('process_money/<start>/<end>',views.process_money),
    path('reset',views.reset)
]