from django import forms
from .models import Student_data_insert, Teacher_data_insert

class StudentInsertDataForm(forms.ModelForm):
    class Meta:
        model = Student_data_insert
        fields = ["name", "RollNo", "Mail", "Password"]

class TeacherInsertDataForm(forms.ModelForm):
    class Meta:
        model = Teacher_data_insert
        fields = ["name", "Teacher_ID", "Mail", "Password"]

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student_data_insert
        fields = ["RollNo", "Password"]