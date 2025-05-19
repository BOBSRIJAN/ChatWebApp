from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('chat/', views.home, name='home'),
    path('messages/', views.messages_api, name='messages_api'),
    path('logout/', views.logout_view, name='logout'),
    path('UsClear/', views.UsClear, name='UsClear'),
]
    