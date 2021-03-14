
from django.urls import path, include
from . import views
from .import AdminView
urlpatterns = [
    path('', views.loginPage, name="login"),
    path('admin_home/', AdminView.admin_home, name="admin_home"),
    path('admin_profile/', AdminView.admin_profile, name="admin_profile"),
    path('admin_profile_update/', AdminView.admin_profile_update, name="admin_profile_update"),

]
