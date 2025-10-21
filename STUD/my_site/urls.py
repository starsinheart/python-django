from django.urls import path
from . import views 

urlpatterns= [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('add_student', views.add_student, name='add_student'),
    path('students', views.students_list, name='students_list'),
]


