from django.db import models

# Create your models here.
class Subject(models.Model):
    id_subject = models.AutoField(primary_key=True, editable=False)
    code = models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teachers.Teacher', on_delete=models.CASCADE)
    prerequisites = models.ManyToManyField('self', symmetrical=False, related_name='prerequisite_subjects', blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        db_table = 'T401Subject'
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Enrollment(models.Model):
    id_enrollment = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey('Students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()


    class Meta:
        db_table = 'T402Enrollment' 
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"