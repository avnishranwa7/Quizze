from django.contrib import admin
from django.urls import path
from Quiz import views

urlpatterns = [
    path('', views.homepage, name="Home"),
    path('test', views.TestView, name='Test'),
    path('teacher_register/', views.TeacherInsertData, name='teacher_register'),
    path('admin/', views.Admin, name="Admin"),
    path('courses/rollno=<str:rollno>', views.Courses, name='Courses'),
    path('quizzes', views.Quizzes, name='Quizzes'),
    path('result', views.results, name='Result'),
    path('studentlogin', views.Studentlogin, name='student_login'),
    path('home', views.homepage),
    path('signup', views.StudentInsertData, name='signup'),
    # path('questions/<str:quiz_id>/<str:rollno>', views.Question),
]