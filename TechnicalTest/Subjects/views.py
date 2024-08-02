from rest_framework import generics
from .models import Subject,Enrollment,Pensum
from .serializers.subject_serializers import SubjectSerializer
from .serializers.pensum_serializers import PensumSerializer
from .serializers.enrollment_serializers import EnrollmentCreateSerializer,SubjectEstudentsSerializer,SubjectEstudentsapprovedSerializer,SubjectEstudentFailedSerializer,GradeUpdateSerializer,EnrollmentGradeSerializer
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


#1. Un estudiante se inscribe en una lista de materias
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

#2. Un estudiante puede obtener la lista de materias en las que está inscrito.
class StudentEnrollmentsList(generics.ListAPIView):
    serializer_class = SubjectEstudentsSerializer

    def get_queryset(self):
        
        student_id = self.kwargs['student_id']
       
        return Enrollment.objects.filter(student_id=student_id)
    




#3. Un estudiante aprueba una materia con una nota igual o mayor a 3.0.

#4 Un estudiante puede obtener la lista de sus materias aprobadas y su promediode puntaje general.

class StudentApprovedSubjectsList(generics.ListAPIView):
    serializer_class = SubjectEstudentsapprovedSerializer

    def get(self,kwargs,student_id):
       
        student_id = student_id


        enrollments = Enrollment.objects.filter(student=student_id, grade__isnull=False)
        approved = enrollments.filter(grade__gte=3)
      
        subject_ids = approved.values_list('subject_id', flat=True)
        average_grade = enrollments.aggregate(Avg('grade'))['grade__avg']

        # subjects = Subject.objects.filter(id_subject__in=subject_ids)
        serializer = self.serializer_class(approved,many=True)
        data={}
        data['subjects'] =serializer.data
        data['average'] =average_grade
        return Response(data)
    


#5. Comprobar las materias que un estudiante ha reprobado.

class StudentFailedSubjectsList(generics.ListAPIView):
    serializer_class = SubjectEstudentFailedSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']  
        return Enrollment.objects.filter(student_id=student_id, grade__lt=3, grade__isnull=False)
    

#9. Un profesor finaliza la materia (califica cada estudiante)
class GradeUpdateView(generics.UpdateAPIView):
    serializer_class = GradeUpdateSerializer

    def update(self, request,id_student,id_subject):
        data = request.data
        instance = Enrollment.objects.filter(subject_id=id_subject,student=id_student).first()
        serializer = self.serializer_class(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


#10. Un profesor puede obtener las calificaciones de los estudiantes en sus materias

class SubjectEnrollmentGradeView(generics.ListAPIView):
    serializer_class = EnrollmentGradeSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']  
        return Enrollment.objects.filter(subject_id=subject_id)