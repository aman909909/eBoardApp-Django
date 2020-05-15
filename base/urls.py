from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='base/password_reset.html'
            ),
            name='password_reset'),

    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='base/password_reset_done.html'
            ),
            name='password_reset_done'),    

    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='base/password_reset_confirm.html'
            ),
            name='password_reset_confirm'), 

    path('password-reset/complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='base/password_reset_complete.html'
            ),
            name='password_reset_complete'),    

    path('carddetail/<int:z>', views.cardDetail, name="card_page"),
    path('cardcomment/<int:z>', views.cardcmnt, name="card_comment"),
    path('deletecard/<int:z>', views.cardDelete, name="card_delete"),
    

]
