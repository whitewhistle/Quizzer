
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="login"),
    path('sign-up', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('createQuiz', views.createQuiz , name="createQuiz")
    
]