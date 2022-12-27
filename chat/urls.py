from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.room, name='room'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout')
]