from django.contrib import admin
from django.urls import path
from Quiz import views

urlpatterns = [
    path('', views.homepage, name="Home"),
    path('test/<str:rollno>/<str:quiz_id>/<str:time>', views.TestView),
    path('teacher_register/', views.TeacherInsertData),
    path('admin/', views.Admin, name="Admin"),
    path('courses/<str:rollno>', views.Courses, name='Courses'),
    path('quizzes/<str:Course_ID>/<str:rollno>', views.Quizzes),
    path('result/<str:rollno>/<str:quiz_id>', views.results),
    path('studentlogin', views.Studentlogin),
    path('home', views.homepage),
    path('signup', views.StudentInsertData),
    # path('questions/<str:quiz_id>/<str:rollno>', views.Question),
]