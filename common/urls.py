from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name="signup"),
    path('kakaologin/', views.kakao_login, name="kakaologin"),
    path('kakaologin/callback/', views.kakao_login_callback, name="kakao_callback"),
    # path('login/kakaologin/', views.kakao_login_redirect, name="kakao_login"),
]