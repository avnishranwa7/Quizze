from django.contrib import admin
from .models import Course, enrolled, Student_data_insert
from django.contrib.admin import ModelAdmin
from django.contrib.contenttypes.models import ContentType
from guardian.shortcuts import assign_perm
# Register your models here.

class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('Course_ID', 'RollNo')
    list_filter = (
        ('Course_ID', admin.RelatedOnlyFieldListFilter),
    )

content_type = ContentType.objects.get_for_model(Course)
permission = Permission.objects.create(
    codename='Course',
    name='Can Change Course',
    content_type=content_type,
)

admin.site.register(Course)
admin.site.register(enrolled, EnrolledAdmin)