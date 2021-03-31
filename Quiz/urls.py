from django.contrib import admin
from django.urls import path
from Quiz import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('student_register/', views.StudentInsertData),
    path('teacher_register/', views.TeacherInsertData),
    path('student_signin/', views.Student_login, name="student_sign_in"),
    path('admin/', views.Admin, name="Admin"),
    path('courses/<str:rollno>', views.Courses, name='Courses'),
    path('quizzes/<str:Course_ID>/<str:rollno>', views.Quizzes),
    path('questions/<str:quiz_id>/<str:rollno>', views.Question),
]