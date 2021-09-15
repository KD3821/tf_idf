from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.get_file, name='our_form'),
    path('res/', views.get_idf, name='get_w'),
    path('form_n/', views.get_new, name='next_f'),
]