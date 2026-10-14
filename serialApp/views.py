from django.shortcuts import render
from rest_framework import viewsets
from serialApp.models import Student
from serialApp.serializers import StudentSerializer
# Create your views here.
class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer