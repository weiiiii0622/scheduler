from django.contrib.auth import views as auth_views
from django.urls import path
from .views import homepage, User_register, User_login, User_logout,Grades

urlpatterns = [
    path('', homepage, name='mainsite-home'),
    path('register/', User_register, name='mainsite-register'),
    path('login/', User_login, name='mainsite-login'),
    path('logout/', User_logout, name='mainsite-logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "mainsite/password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "mainsite/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "mainsite/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "mainsite/password_reset_complete.html"),  name='password_reset_complete'),
    path('grades/',Grades,name='grades'),
]