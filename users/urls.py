from django.urls import path,reverse_lazy
from .views import dashboard, register, edit
from django.contrib.auth.views import(LoginView,LogoutView,PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordChangeDoneView,PasswordChangeView,PasswordContextMixin,PasswordResetCompleteView)
app_name = 'users'
urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register,name='register'),
    path('edit/',edit,name='edit'),
    path('',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('password_change/',PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'),name='password_changed'),
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset_form.html',email_template_name='registration/password_reset_email.html',success_url=reverse_lazy('users:password_reset_done')),name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password-reset-done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('registration:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]

