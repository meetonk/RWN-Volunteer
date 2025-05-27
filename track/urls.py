from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.application_list, name="application_list"),
    path("add", views.application_create, name="application_create"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # login page
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('status/add/', views.status_create, name='status_create'),
    path('status/add/<int:app_id>/', views.add_status_update, name='add_status_update'),
    path('application/<int:pk>/delete/', views.application_delete, name='application_delete'),
    path('status/update/<int:pk>/delete/', views.status_update_delete, name='status_update_delete'),
    path('status/<int:pk>/delete/', views.status_delete, name='status_delete'),

    path('export_excel/', views.export_applications_excel, name='export_excel'),

]