from django.contrib import admin
from django.urls import path
from Quiz import views

urlpatterns = [
    path('student_register/', views.StudentInsertData),
    path('teacher_register/', views.TeacherInsertData),
]