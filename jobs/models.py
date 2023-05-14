from django.conf import settings
from django.db import models
from django_lifecycle import LifecycleModelMixin, hook, AFTER_CREATE, AFTER_UPDATE

from .mailing import send_job_created_mail, send_job_updated_mail


# Create your models here.
class Job(LifecycleModelMixin, models.Model):
    FULL_TIME = 'full-time'
    PART_TIME = 'part-time'

    JOB_TYPES = (
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=JOB_TYPES)

    def __str__(self):
        return self.name

    @hook(AFTER_CREATE)
    def on_create(self):
        send_job_created_mail(self.id)


class JobHeader(LifecycleModelMixin, models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='header')
    rich_title_text = models.TextField()
    rich_subtitle_text = models.TextField()

    def __str__(self):
        return self.job.name

    @hook(AFTER_UPDATE)
    def on_update(self):
        old_title_rich_text = self.initial_value('rich_title_text')
        send_job_updated_mail(self.job.id, old_title_rich_text, self.rich_title_text)


class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username} | Job: {self.job.name}"
