from django.shortcuts import render
from .serializers.students_serializers import StudentSerializer
from .models import Student
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
