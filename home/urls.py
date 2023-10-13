from django.urls import path
from . import views
#vi file views minh viet & file cua django cung ten nen can doi lại ten cho no la auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('contact/',views.contact, name = 'contact'),
    path('register/',views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name = 'logout'),
]

