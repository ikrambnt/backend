from django.urls import path

from accounts import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
app_name = "accounts"


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
    path("changepassword/", views.PasswordsChangeView.as_view(template_name='accounts/changepassword.html'),name="change_password"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("update_user/<int:pk>", views.update_user, name='update_user'),
    path("Admin_update_user/<int:user_id>", views.update_user_admin, name='update_user_byadmin'),
    path("list_users/", views.list_users, name='list_users'),
    
   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]
