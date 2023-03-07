from django.urls import path
from roles import views

urlpatterns = [
    path('roles/', views.RoleList.as_view()),
]