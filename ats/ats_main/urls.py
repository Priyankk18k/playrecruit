from django.urls import path
from ats_main import views

urlpatterns = [
    path('', views.vw_index, name='ats_main'),
]
