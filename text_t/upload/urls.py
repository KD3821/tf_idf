from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.get_file, name='our_form'),
    # path('file/', views.get_file, name='get_form'),
    # path('form_no/', views.no_form, name='not_f'),
]