from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from authapp.views import SchoolUserCreateView


app_name = 'authapp'

urlpatterns = [
    path('register/', SchoolUserCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(
        template_name='authapp/login.html',
        success_url=reverse_lazy('main:index')
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
