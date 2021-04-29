from django import forms
from .models import Student_data_insert, Teacher_data_insert, responses

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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = responses
        fields = ["RollNo", "q_id", "response"]

class TestForm(forms.ModelForm):
    responses = forms.CharField()
    class Meta:
        model = responses
        fields = ('response', )

# class Mark(forms.ModelForm):
#     class Meta:
