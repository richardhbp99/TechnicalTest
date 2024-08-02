from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Subjects.serializers.subject_serializers import SubjectSerializer
from Teachers.serializers.teachers_serializers import StudentSubjectSerializer

from Subjects.models import Enrollment, Subject
from Students.models import Student
# Create your views here.


#6. Un profesor puede tener asignadas varias materias
#7. Un profesor puede obtener las lista de materias a las que esta asignado

class TeacherAssignedSubjectsList(generics.ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Obtén el ID del profesor de los parámetros de la URL
        teacher_id = self.kwargs['teacher_id']
        
        # Filtra las materias asignadas al profesor
        return Subject.objects.filter(teacher_id=teacher_id)


#8. Un profesor puede ver la lista de estudiantes de cada una de sus materias

class SubjectStudentsList(generics.ListAPIView):
    serializer_class = StudentSubjectSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Obtén el ID de la materia de los parámetros de la URL
        subject_id = self.kwargs['subject_id']
        
        # Filtra las inscripciones por el ID de la materia y obtiene los IDs de los estudiantes
        student_ids = Enrollment.objects.filter(subject=subject_id).values_list('student', flat=True)
        
        # Obtén los estudiantes relacionados con los IDs obtenidos
        return Student.objects.filter(id_student__in=student_ids)
