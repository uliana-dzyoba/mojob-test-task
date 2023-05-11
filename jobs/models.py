from django.conf import settings
from django.db import models


# Create your models here.
class Job(models.Model):
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


class JobHeader(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    rich_title_text = models.TextField()
    rich_subtitle_text = models.TextField()

    def __str__(self):
        return self.job.name


class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username} | Job: {self.job.name}"
