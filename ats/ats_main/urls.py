from django.urls import path
from ats_main import views

urlpatterns = [
    path('', views.vw_index, name='ats_main'),
    # path('candidate/', views.vw_data, name='candidate')
    path('candidate/', views.vw_download, name='candidate'),
    path('mail/', views.vw_email, name='mail'),
]
