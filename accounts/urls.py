from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('', views.home, name='home'),
    path('patient/<str:pk>/', views.patient, name='patient'),

    path('create_patient/', views.create_patient, name='create_patient'),
    path('update_patient/<str:pk>/', views.update_patient, name='update_patient'),

    path('create_diagnosis/<str:pk>/', views.create_diagnosis, name='create_diagnosis'),
    path('update_diagnosis/<str:pk>/', views.update_diagnosis, name='update_diagnosis'),

    path('create_checkup/<str:pk>/', views.create_checkup, name='add_check_up'),
    path('update_checkup/<str:pk>/', views.update_checkup, name='update_checkup'),
    
    path('create_allergy/<str:p_id>/', views.create_allergy, name='create_allergy'),
    path('update_allergy/<str:pk>/<str:p_id>/', views.update_allergy, name='update_allergy'),

    path('new_appointment/', views.create_appointment, name='new_appointment'),

    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    
]