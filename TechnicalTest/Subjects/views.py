from rest_framework import generics
from .models import Subject,Enrollment,Pensum
from .serializers.subject_serializers import SubjectSerializer
from .serializers.pensum_serializers import PensumSerializer
from .serializers.enrollment_serializers import EnrollmentCreateSerializer,SubjectEstudentsSerializer,SubjectEstudentsapprovedSerializer
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.response import Response
from django.db.models import Avg

# Create your views here.
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class PensumListViews(generics.ListAPIView):
    queryset = Pensum.objects.all()
    serializer_class = PensumSerializer 

class EnrollmentCreateViews(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class= EnrollmentCreateSerializer

    def post(self, request):
        data_in = request.data

        if  not 'id_pensum' in data_in:
            raise ValidationError("no pensum found")
        
        pensum = Pensum.objects.filter(id_pensum=data_in['id_pensum']).first()
        

        if not pensum:
            raise NotFound("")
        
        subjects = pensum.subjects.all()

 
        data_enrollment=[]
        
        for subject in subjects:
            
            
            data_enrollment.append({
                "date": "2024-08-02",
                "student": data_in['student'],
                "subject": subject.id_subject
                })
        serializer = self.serializer_class(data=data_enrollment,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class StudentEnrollmentsList(generics.ListAPIView):
    serializer_class = SubjectEstudentsSerializer

    def get_queryset(self):
        # Obtén el ID del estudiante de los parámetros de la URL
        student_id = self.kwargs['student_id']
        # Filtra las inscripciones por el ID del estudiante
        return Enrollment.objects.filter(student_id=student_id)
    





class StudentApprovedSubjectsList(generics.ListAPIView):
    serializer_class = SubjectEstudentsapprovedSerializer

    def get(self,kwargs,student_id):
        # Obtén el ID del estudiante de los parámetros de la URL
        student_id = student_id


        enrollments = Enrollment.objects.filter(student=student_id, grade__isnull=False)
      
        subject_ids = enrollments.values_list('subject_id', flat=True)
        average_grade = enrollments.aggregate(Avg('grade'))['grade__avg']

        subjects = Subject.objects.filter(id_subject__in=subject_ids)
        serializer = self.serializer_class(subjects,many=True)
        data={}
        data['subjects'] =serializer.data
        data['average'] =average_grade
        return Response(data)