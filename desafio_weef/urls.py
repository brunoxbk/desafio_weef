from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import UserCreate, CustomLogin
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', UserCreate.as_view(), name='sign_up'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='users/logged_out.html',
            next_page=reverse_lazy('login')),
        name='logout'),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            extra_email_context={'title': 'Recuperação de senha'},
            template_name="auth/password_reset_form.html",
            email_template_name="auth/password_reset_email.html",
            html_email_template_name="auth/password_reset_email.html",
            subject_template_name="auth/password_reset_subject.txt",
            success_url=reverse_lazy('password_reset_done'),
        ),
        name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset_done.html"),
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html",
            success_url='password_reset/done/'),
        name='password_reset_confirm'),
    path('', include('todo.urls', namespace='todo')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
