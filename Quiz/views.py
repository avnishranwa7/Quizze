from django.shortcuts import render
from Quiz.models import Student_data_insert
from django.contrib import messages
from .forms import StudentInsertDataForm, TeacherInsertDataForm

def StudentInsertData(request):
    form = StudentInsertDataForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'DataForm': StudentInsertDataForm}
    return render(request, "student\\student_register.html", context)

def TeacherInsertData(request):
    form = TeacherInsertDataForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'DataForm': TeacherInsertDataForm}
    return render(request, "teacher\\teacher_register.html", context)