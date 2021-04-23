from django.db import models
from composite_field import CompositeField


class Student_data_insert(models.Model):
    name = models.CharField(max_length = 20, null=False)
    RollNo = models.CharField(primary_key = True, max_length = 20)
    Mail = models.CharField(max_length = 30, null=False)
    Password = models.CharField(max_length = 20, null=False)
    class Meta:
        db_table = "students"

    def __str__(self):
        return self.RollNo

class Teacher_data_insert(models.Model):
    name = models.CharField(max_length = 20, null=False)
    Teacher_ID = models.CharField(primary_key = True, max_length = 20)
    Mail = models.CharField(max_length = 30, null=False)
    Password = models.CharField(max_length = 20, null=False)
    class Meta:
        db_table = "teacher"

class Course(models.Model):
    Course_ID = models.CharField(primary_key = True, max_length=10)
    Course_Name = models.CharField(max_length=30, null=False)
    class Meta:
        db_table = "Courses"
        
    def __str__(self):
        return "{}".format(self.Course_ID)

class enrolled(models.Model):
    id = models.AutoField(primary_key = True)
    Course_ID = models.ForeignKey(Course, on_delete = models.CASCADE, db_column = 'Course_ID', null=False)
    RollNo = models.ForeignKey(Student_data_insert, on_delete = models.CASCADE, db_column = 'RollNo', null=False)
    class Meta:
        db_table = "enrolled"
        verbose_name = "Enrolled Student"

    def __str__(self):
        return "{} - {}".format(self.RollNo, self.Course_ID)

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key = True)
    quiz_name = models.CharField(max_length = 20, null=False)
    Course_ID = models.ForeignKey(Course, on_delete = models.CASCADE, db_column = 'Course_ID', null=False)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    duration = models.IntegerField(null=False)
    class Meta:
        db_table = "Quiz"
        verbose_name = "Quizze"

    def __str__(self):
        return str(self.quiz_id)

class Questions(models.Model):
    choices = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    q_id = models.AutoField(primary_key = True)
    quiz_id = models.ForeignKey(Quiz, on_delete = models.CASCADE, db_column = 'quiz_id', null=False)
    question = models.CharField(max_length = 500, null=False)
    opt1 = models.CharField(max_length = 100, null=False)
    opt2 = models.CharField(max_length = 100, null=False)
    opt3 = models.CharField(max_length = 100, null=True, blank = True)
    opt4 = models.CharField(max_length = 100, null=True, blank = True)
    ans = models.CharField(max_length = 1, null=False, choices = choices)
    class Meta:
        db_table = "Questions"
        verbose_name = "Question"

    def __str__(self):
        return self.question


class responses(models.Model):
    id = models.AutoField(primary_key = True)
    RollNo = models.ForeignKey(Student_data_insert, on_delete = models.CASCADE, db_column = 'RollNo', null=False)
    q_id = models.ForeignKey(Questions, on_delete = models.CASCADE, db_column = 'q_id', null=False)
    response = models.CharField(max_length = 1, null=False)
    class Meta:
        db_table = "responses"
        verbose_name = "Response"
        unique_together = ('RollNo', 'q_id',)