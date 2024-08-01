from django.db import models



# Create your models here.
class Estudent(models.Model):
    id_student = models.AutoField(primary_key=True, editable=False)
    code = models.CharField(max_length=200 ,unique=True)
    person = models.OneToOneField('Security.Person', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'T201Estudent'
