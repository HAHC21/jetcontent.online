from django.urls import path

from core.views import *

urlpatterns = [
    path('', index),
    path('site/<int:id>', show, name='site'),
    path('article/<int:id>', article, name='article'),
    path('import/<int:id>', import_posts, name='import'),
]
