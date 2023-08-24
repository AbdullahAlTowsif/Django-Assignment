# from django.urls import path
# from .views import index

# app_name = 'mealapp'  # This sets the app namespace

# urlpatterns = [
#     path('', index, name='index'),
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = "indexpage"),
]
