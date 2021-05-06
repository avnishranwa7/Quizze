from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentInsertDataForm, TeacherInsertDataForm, StudentLoginForm, QuestionForm, TestForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Student_data_insert, enrolled, Course, Quiz, Questions, responses, marks_db, test
from django.contrib.auth import authenticate, login, logout
import mysql.connector
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from json import dumps
import json
import datetime
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home\home.html')

def Studentlogin(request):
    if request.method=='POST':
        RollNo = request.POST.get('rollno')
        Password = request.POST.get('pass')
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="sakila"
        )
            
        mycursor = mydb.cursor()

        mycursor.execute("SELECT RollNo, Password FROM students WHERE RollNO = '"+RollNo+"' and Password = '" + Password + "'")
            
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            messages.error(request, "Invalid Username/Password")
        else:
            return redirect('courses/rollno='+RollNo)
    return render(request, "Login_v1\index.html")

def Home(request):
    return render(request, "welcome.html")

def Courses(request, rollno):
    course = enrolled.objects.all().filter(RollNo = rollno)
    student_obj = Student_data_insert.objects.all().filter(RollNo = rollno).first()
    con = {'course': course, 'student_obj': student_obj, 'rollno': rollno}
    return render(request, "student_courses\courses2.html", con)

def Quizzes(request):
    Course_ID = request.GET.get('course_id')
    rollno = request.GET.get('rollno')
    quiz = Quiz.objects.all().filter(Course_ID = Course_ID)
    bool_list = []
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="sakila"
    )
            
    mycursor = mydb.cursor()

    for i in quiz:
        mycursor.execute("SELECT * FROM results WHERE RollNO = '"+rollno+"' and quiz_id = '" + str(i.quiz_id) + "'")
        myresult = mycursor.fetchall()
        if datetime.datetime.combine(i.date, i.start_time) <= datetime.datetime.now():
            if datetime.datetime.combine(i.date, i.end_time) > datetime.datetime.now():
                if len(myresult):
                    bool_list.append((i, "locked"))
                else:
                    bool_list.append((i, "active"))
            else:
                bool_list.append((i, "over"))
        else:
            bool_list.append((i, "locked"))
        
    con = {'bool': bool_list, 'rollno': rollno}
    return render(request, "quizzes\quizzes2.html", con)

def Add_Data(RollNo, q_id, response):
    responses.objects.create(RollNo = RollNo, q_id = q_id, response = response)

def TestView(request):
    quiz_id = request.GET.get('quiz_id')
    rollno = request.GET.get('rollno')
    time = request.GET.get('t_id')
    print(time)
    ques = Questions.objects.all().filter(quiz_id = quiz_id)
    quiz_obj = Quiz.objects.get(quiz_id = quiz_id)
    l = len(ques)
    s = Student_data_insert.objects.get(pk = rollno)
    # s = Student_data_insert.objects.get(pk = rollno)
    QuestionFormSet = modelformset_factory(test, fields=('response',), can_delete = True, extra = l)
    if request.method=='POST':
        form = QuestionFormSet(request.POST, queryset = Student_data_insert.objects.filter(RollNo = rollno))
        if form.is_valid():
            instances = form.save(commit = False)
            mark = 0
            for instance,q in zip(instances, ques):
                if instance.response == q.ans:
                    mark += 1
                instance.RollNo = s
                instance.q_id = q
                instance.save()
                Add_Data(s, q, instance.response)
            for instance in instances:
                instance.delete()
                
            marks_object = marks_db.objects.create(RollNo = s, quiz_id = quiz_obj, marks = mark)
            if not request.GET._mutable:
                request.GET._mutable = True
            request.GET['course_id']=quiz_obj.Course_ID
            request.GET['rollno']=rollno
            return Quizzes(request)

        
    form = QuestionFormSet()
    return render(request, 'test.html', {'form_ques': zip(list(form), list(ques)), 'form': form, 'quiz_obj': quiz_obj, 
    'time': json.dumps(time)})

def results(request):
    rollno = request.GET.get('rollno')
    quiz_id = request.GET.get('quiz_id')
    marks_obj = marks_db.objects.all().filter(RollNo = rollno, quiz_id=quiz_id).first()
    ques = Questions.objects.all().filter(quiz_id = quiz_id)
    response_list = []
    quiz_obj = Quiz.objects.get(quiz_id = quiz_id)
    if marks_obj is not None:
        for i in ques:
            response_list.append(responses.objects.all().filter(RollNo = rollno, q_id = i.q_id).first().response)
        return render(request, 'results.html', {'quiz_obj': quiz_obj, 'marks':marks_obj.marks, 'ques': zip(ques, response_list), 'course': quiz_obj.Course_ID, 'rollno': rollno})
    else:
        return render(request, 'error\error.html', {'course': quiz_obj.Course_ID, 'rollno': rollno})

def Question(request, quiz_id, rollno):
    ques = Questions.objects.all().filter(quiz_id = quiz_id)
    quiz_obj = Quiz.objects.get(quiz_id = quiz_id)
    s = Student_data_insert.objects.get(pk = rollno)
    # s = Student_data_insert.objects.get(pk = rollno)
    QuestionFormSet = modelformset_factory(responses, fields=('response',), extra=3)
    
    
    if request.method=='POST':
        form = QuestionFormSet(request.POST, queryset = Student_data_insert.objects.filter(RollNo = rollno))
        if form.is_valid():
            instances = form.save(commit = False)
            for instance,q in zip(instances, ques):
                instance.RollNo = s
                instance.q_id = q
                temp = instance
                instance.save()
            return redirect('http://127.0.0.1:8000/test/{}/{}'.format(temp.q_id.quiz_id.Course_ID, rollno))

        print(form.errors)
    form = QuestionFormSet()
    return render(request, 'test.html', {'form_ques': zip(list(form), list(ques)), 'form': form, 'quiz_obj': quiz_obj})

def Admin(request):
    return render(request, 'Admin')

def StudentInsertData(request):
    form = StudentInsertDataForm(request.POST or None)
    pass1 = request.POST.get('Password')
    pass2 = request.POST.get('confirmpass')
    if(pass1!=pass2):
        messages.error(request, "Password did not match!")
    else:
        if request.method=='POST':
            RollNo = str(request.POST.get('RollNo'))
            Mail = str(request.POST.get('Mail'))
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="sakila"
            )                  
            mycursor = mydb.cursor()

            mycursor.execute("SELECT RollNo FROM students")
                                
            myresult = mycursor.fetchall()
            if (RollNo,) in myresult:
                messages.error(request, "Student with same Roll Number already exists!")
            else:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT Mail FROM students")
                myresult = mycursor.fetchall()
                if (Mail,) in myresult:
                    messages.error(request, "Mail already taken!")
                else:
                    if form.is_valid():
                        form.save()
                        return redirect(Studentlogin)
    context = {'DataForm': StudentInsertDataForm}
    return render(request, "Signup_v1\signup.html", context)

def TeacherInsertData(request):
    form = TeacherInsertDataForm(request.POST or None)
    pass1 = request.POST.get('Password')
    pass2 = request.POST.get('confirmpass')
    if(pass1!=pass2):
        messages.error(request, "Password did not match!")
    else:
        if request.method=='POST':
            Teacher_ID = str(request.POST.get('Teacher_ID'))
            Mail = str(request.POST.get('Mail'))
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="sakila"
            )
                                
            mycursor = mydb.cursor()

            mycursor.execute("SELECT Teacher_ID FROM teacher")
                                
            myresult = mycursor.fetchall()
            if (Teacher_ID,) in myresult:
                messages.error(request, "Teacher with same Teacher_ID already exists!")
            else:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT Mail FROM teacher")
                myresult = mycursor.fetchall()
                if (Mail,) in myresult:
                    messages.error(request, "Mail already taken!")
                else:
                    if form.is_valid():
                        user = User.objects.create_user(form.cleaned_data['Teacher_ID'], form.cleaned_data['Mail'], form.cleaned_data['Password'], is_staff = True)
                        user.save()
                        teacher = Group.objects.get(name='Teachers') 
                        teacher.user_set.add(user)
                        form.save()
                        return redirect(Admin)
                        

    context = {'DataForm': TeacherInsertDataForm}
    return render(request, "Teacher_signup\\teacher_signup.html", context)


    
