from django.utils.html import strip_tags
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Job, JobHeader, Application


class JobInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobHeaderSerializer(serializers.ModelSerializer):
    plain_title_text = serializers.SerializerMethodField()

    class Meta:
        model = JobHeader
        fields = ('rich_title_text', 'rich_subtitle_text', 'plain_title_text')

    def get_plain_title_text(self, obj):
        return strip_tags(obj.rich_title_text)


class JobSerializer(WritableNestedModelSerializer):
    header = JobHeaderSerializer()

    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        job_header_data = validated_data.pop('header')
        job = Job.objects.create(**validated_data)
        JobHeader.objects.create(job=job, **job_header_data)
        return job


class ApplicationSerializer(serializers.ModelSerializer):
    job = JobInlineSerializer(read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
