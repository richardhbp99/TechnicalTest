from rest_framework import serializers
from Subjects.models import Enrollment, Subject
from Students.models import Student
from .subject_serializers import SubjectSerializer

class SubjectEstudentsSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer()
    class Meta:
        model = Enrollment
        fields = ['subject']

class SubjectEstudentsapprovedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'



class EnrollmentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enrollment
        fields = '__all__'

    def validate(self, data):
        # Accede al valor de 'grade' desde los datos recibidos
        subject = data.get('subject')
        student = data.get('student')

     

        prerequisites = subject.prerequisites.all()

       
        for prerequisite in prerequisites:

            enrollment= Enrollment.objects.filter(student=student,subject=prerequisite).first()
          
         
            if not enrollment:
                raise serializers.ValidationError("The student has not enrolled "+prerequisite.name)
            if  not enrollment.grade :
                raise serializers.ValidationError("The student has not completed the course "+prerequisite.name)
            if enrollment.grade < 3:
                raise serializers.ValidationError("Student has not passed  "+prerequisite.name)
        
        return data