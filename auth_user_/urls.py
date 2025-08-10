
from django.urls import path

from .views import *

urlpatterns = [
    path('regis/', RegisterApi.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('logout/',LogutApi.as_view(),name='logut'),
]