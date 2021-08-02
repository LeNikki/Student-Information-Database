#from django.forms import ModelForm, Textarea
from django.db import models


# Create your models here.
class App1Students(models.Model):
    no_field = models.AutoField(primary_key=True)
    sid = models.IntegerField(db_column='sId')  # Field name made lowercase.
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45) 
    email = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    yr_sec = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'app1_students'

    def __int__ (self):
        return self.sid  #returns student ID

#We need to make migrations for this model 
#then migrate it to the database
#for every cahnges, make migrations, to make mig. files
#  then apply by manage.py migrate
