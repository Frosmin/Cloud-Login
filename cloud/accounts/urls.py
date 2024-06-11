
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MensageView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('mensage/', auth_views.LogoutView.as_view(), name='mensage'),
    path('mensage/', MensageView.as_view(), name='mensage'),
]
