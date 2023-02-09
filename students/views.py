from django.shortcuts import render
from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get']


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get']
