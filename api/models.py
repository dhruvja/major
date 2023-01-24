import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admission(models.Model):
    YEAR_CHOICES = [(str(r), str(r)) for r in range(2010, datetime.date.today().year+1)]
    SEMESTER_CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"),("7", "7"), ("8", "8")] 
    semester = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
    batch = models.CharField(max_length=255, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    cet = models.IntegerField(default = 0)
    comedk = models.IntegerField(default = 0)
    management = models.IntegerField(default = 0)
    diploma = models.IntegerField(default = 0)
    cob = models.IntegerField(default = 0)

    def __str__(self):
        return self.semester

    class Meta:
        verbose_name_plural = 'Admission'

class AdmissionFile(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='admission')
    name = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.name
