from django.contrib import admin

from .models import Job, JobHeader, Application


# Register your models here.

@admin.register(JobHeader)
class JobHeaderAdmin(admin.ModelAdmin):
    raw_id_fields = ('job',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'job',)


admin.site.register(Job)
