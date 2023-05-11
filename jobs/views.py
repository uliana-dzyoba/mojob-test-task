from rest_framework import generics

from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer


# Create your views here.
class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class UserApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs.get('user_pk'))
