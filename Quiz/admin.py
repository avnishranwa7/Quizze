from django.contrib import admin
from .models import Course, enrolled, Student_data_insert
from django.contrib.admin import ModelAdmin
# Register your models here.

class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('Course_ID', 'RollNo')
    list_filter = (
        ('Course_ID', admin.RelatedOnlyFieldListFilter),
    )



admin.site.register(Course)
admin.site.register(enrolled, EnrolledAdmin)