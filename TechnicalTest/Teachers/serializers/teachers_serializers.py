from Subjects.models import Subject
from Teachers.models import Teacher
from rest_framework import serializers

from Students.models import Student

class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'