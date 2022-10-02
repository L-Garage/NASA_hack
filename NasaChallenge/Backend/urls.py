from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.main),
    path('create',views.create)
]