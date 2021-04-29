from django.contrib import admin
from .models import Course, enrolled, Student_data_insert, Quiz, Questions, marks_db
from django.contrib.admin import ModelAdmin
# Register your models here.




class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('Course_ID', 'RollNo')
    list_filter = (
        ('Course_ID', admin.RelatedOnlyFieldListFilter),
    )

class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'quiz_name', 'Course_ID','start_time', 'end_time', 'duration')
    list_filter = (
        ('Course_ID', admin.RelatedOnlyFieldListFilter),
    )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'opt1', 'opt2', 'opt3', 'opt4', 'ans')
    list_filter = (
        ('quiz_id', admin.RelatedOnlyFieldListFilter),
    )



class MarksAdmin(admin.ModelAdmin):
    list_display = ('RollNo', 'quiz_id', 'marks')
    list_filter = (
        ('quiz_id', admin.RelatedOnlyFieldListFilter),
    )

admin.site.register(Course)
admin.site.register(enrolled, EnrolledAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(marks_db, MarksAdmin)