from django.contrib import admin

from .models import Job, JobHeader, Application

# Register your models here.
admin.site.register(Job)
admin.site.register(JobHeader)
admin.site.register(Application)
