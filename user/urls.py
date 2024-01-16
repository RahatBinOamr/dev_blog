from django.urls import path
from user.views import Register,LogOut,Profile,UpdateProfile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',Register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogOut, name='logout'),
    path('profile/', Profile, name='profile'),
    path('update_profile/', UpdateProfile, name='update_profile'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),

    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),
]
