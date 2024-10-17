from django.urls import path
from . import views

urlpatterns = [
    # path('', views.chat),
    path('', views.createRoom),
    path('<str:room_name>/<str:user_name>', views.messageView, name='chat')
]
