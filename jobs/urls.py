from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobCreateView.as_view(), name='create_job'),
    path('jobs/<int:pk>/', views.JobDetailUpdateDeleteView.as_view(), name='job'),
    path('applications/<int:user_pk>/', views.UserApplicationListView.as_view(), name='user_applications'),
]