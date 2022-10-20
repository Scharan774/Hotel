from django.urls import path
from  . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('HungryHorse',views.HungryHorse,name='HungryHorse'),
    path('HungryHorse1',views.HungryHorse1,name='HungryHorse1'),
    path('final',views.final,name='final'),
    path('final1',views.final1,name='final1'),
    ]