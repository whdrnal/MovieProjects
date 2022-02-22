from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # 아이디 찾기
    path('find_username/', views.find_username, name='find_username'),

    # 비밀번호 찾기
    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('common:password_reset_complete'),
                                              email_template_name='common/password_reset_email.html',
                                              template_name='common/password_reset_form.html'),
         name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('common:password_reset_complete')),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='common/password_reset_complete.html'),
         name='password_reset_complete'),
    # 비번찾기 끝
]
