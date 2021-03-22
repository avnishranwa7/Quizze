from django.db import models

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
        return self.Course_ID

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
        return self.quiz_name