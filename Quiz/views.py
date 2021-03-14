from django.shortcuts import render, redirect
from Quiz.models import Student_data_insert
from django.contrib import messages
from .forms import StudentInsertDataForm, TeacherInsertDataForm, StudentLoginForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Student_data_insert
from django.contrib.auth import authenticate, login, logout
import mysql.connector
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

def Home(request):
    return render(request, "welcome.html")

def StudentInsertData(request):
    form = StudentInsertDataForm(request.POST or None)
    pass1 = request.POST.get('Password')
    pass2 = request.POST.get('ConfirmPassword')
    if(pass1!=pass2):
        messages.error(request, "Password did not match!")
    else:
        if request.method=='POST':
            RollNo = str(request.POST.get('RollNo'))
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
                messages.error(request, "Roll Number already exists!")
            else:
                if form.is_valid():
                    form.save()

    context = {'DataForm': StudentInsertDataForm}
    return render(request, "student\\student_register.html", context)

def TeacherInsertData(request):
    form = TeacherInsertDataForm(request.POST or None)
    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data['Teacher_ID'], form.cleaned_data['Mail'], form.cleaned_data['Password'], is_staff = True)
        user.save()
        teacher = Group.objects.get(name='Teachers') 
        teacher.user_set.add(user)
    if form.is_valid():
        form.save()

    context = {'DataForm': TeacherInsertDataForm}
    return render(request, "teacher\\teacher_register.html", context)

def Student_login(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method=='POST':
            RollNo = request.POST.get('RollNo')
            Password = request.POST.get('Password')
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
                return redirect('Home')

        context = {}
        return render(request, "student_sign_in\student_signin.html", context)
    