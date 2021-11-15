from django.urls import path

from core.views import *

urlpatterns = [
    path('', index),
    path('site/<int:id>', show, name='site'),
]
