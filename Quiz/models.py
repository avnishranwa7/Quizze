from django.db import models

class Student_data_insert(models.Model):
    name = models.CharField(max_length = 20)
    RollNo = models.CharField(max_length = 20)
    Mail = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 20)
    class Meta:
        db_table = "students"

class Teacher_data_insert(models.Model):
    name = models.CharField(max_length = 20)
    Teacher_ID = models.CharField(max_length = 20)
    Mail = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 20)
    class Meta:
        db_table = "teacher"