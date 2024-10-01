from django.urls import path
from .views import signup,user_login
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView



urlpatterns= [
    path('register/', signup, name='user-signup'),
    path('login/',user_login, name='user-login'),
    # path('login/', LoginView.as_view(template_name="accounts/login.html"), name="user-login"),
    path('logout/', LogoutView.as_view(), name="user-logout"), #post
    path('password_reset/', PasswordResetView.as_view(template_name="accounts/forgetPassword.html"), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="accounts/reset_done.html"), name="password_reset_complete"),

]