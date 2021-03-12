from django.db import models

class Student_data_insert(models.Model):
    name = models.CharField(max_length = 20)
    RollNo = models.CharField(primary_key = True, max_length = 20)
    Mail = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 20)
    class Meta:
        db_table = "students"

    def __str__(self):
        return self.RollNo

class Teacher_data_insert(models.Model):
    name = models.CharField(max_length = 20)
    Teacher_ID = models.CharField(primary_key = True, max_length = 20)
    Mail = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 20)
    class Meta:
        db_table = "teacher"

class Course(models.Model):
    Course_ID = models.CharField(primary_key = True, max_length=10)
    Course_Name = models.CharField(max_length=30)
    class Meta:
        db_table = "Courses"
        

    def __str__(self):
        return self.Course_ID

class enrolled(models.Model):
    id = models.AutoField(primary_key = True)
    Course_ID = models.ForeignKey(Course, on_delete = models.CASCADE, db_column = 'Course_ID')
    RollNo = models.ForeignKey(Student_data_insert, on_delete = models.CASCADE, db_column = 'RollNo')
    class Meta:
        db_table = "enrolled"
        verbose_name = "Enrolled Student"

    def __str__(self):
        return "{} - {}".format(self.RollNo, self.Course_ID)