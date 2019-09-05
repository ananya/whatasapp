from django.urls import path
from . import views

urlpatterns = [
    # path('',views.send_msg, name='send_msg'),
    path('msg/new/', views.send_msg, name = 'send_msg'),
    
    # path('',views.add_person, name='add_person'),
]