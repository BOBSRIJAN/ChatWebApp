from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('chat/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('UsClear/', views.UsClear, name='UsClear'),
]
    