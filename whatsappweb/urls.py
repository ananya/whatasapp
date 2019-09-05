from django.urls import path
from . import views

urlpatterns = [
    path('',views.initial_page, name='initial_page'),
    path('msg/new/', views.send_msg, name = 'send_msg'),
    path('employe/new/', views.new_employe, name = 'new_employe'),
    # path('',views.add_person, name='add_person'),
]