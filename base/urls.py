from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home_page"),
    path('login/', views.loginUser, name="login_page"),
    path('signup/', views.signup, name="signup_page"),
    path('logout/', views.logoutUser, name="logout_page"),
    path('newboard/', views.newBoard, name="newboard_page"),
    path('dashboard/', views.dashboard, name="dashboard_page"),
    path('board/<int:z>', views.boardDisplay, name="board_page"),
    path('newlist/<slug:z>', views.newList, name="newlist_page"),
    path('addcard/<int:z>', views.addCard, name="addcard_page"),
    path('deletelist/<int:z>', views.dellist, name="delete_list"),


]
