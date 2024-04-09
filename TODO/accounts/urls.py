from django.urls import path
from . import views
from .views import SignUpView,LoginView,LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signUp/',SignUpView.as_view(),name='signUp'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),


]
