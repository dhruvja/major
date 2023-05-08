import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admission(models.Model):
    YEAR_CHOICES = [(str(r), str(r)) for r in range(2010, datetime.date.today().year+1)]
    admission_year = models.CharField(max_length=255, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    CET = models.IntegerField(default = 0)
    comedk = models.IntegerField(default = 0)
    management = models.IntegerField(default = 0)
    snq = models.IntegerField(default = 0) 
    diploma = models.IntegerField(default = 0)
    CoB_incoming = models.IntegerField(default = 0)
    CoB_outgoing = models.IntegerField(default = 0) 
    total = models.IntegerField(default = 0, blank = True, null=True)

    def __str__(self):
        return "Batch: " + self.admission_year 
    
    def save(self):
        self.total = self.CET + self.comedk + self.management + self.diploma + self.CoB_incoming + self.snq + self.CoB_outgoing 
        return super(Admission, self).save()

    class Meta:
        verbose_name_plural = 'Admission'

class AdmissionFile(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='admission')
    name = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.name

class Result(models.Model):
    YEAR_CHOICES = [(str(r), str(r)) for r in range(2010, datetime.date.today().year+1)]
    SEMESTER_CHOICES = [("1", "1"),("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")] 
    semester = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
    admission_year = models.CharField(max_length=255, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    without_backlog = models.IntegerField(default = 0)
    single_backlog = models.IntegerField(default = 0)
    double_backlog = models.IntegerField(default = 0)
    triple_backlog = models.IntegerField(default = 0)
    more_than_3_backlog = models.IntegerField(default = 0)
    dropouts = models.IntegerField(default = 0)

    def __str__(self):
        return "Batch: " + self.admission_year + " Sem: " + self.semester 

# class ResultFile(models.Model):
#     result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='result')
#     name = models.CharField(max_length=255)
#     file = models.FileField()

#     def __str__(self):
#         return self.name 

class Placement(models.Model):
   YEAR_CHOICES = [(str(r), str(r)) for r in range(2010, datetime.date.today().year+1)] 
   admission_year = models.CharField(max_length=255, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
   on_campus = models.IntegerField(default=0)
   off_campus = models.IntegerField(default=0)
   internship = models.IntegerField(default=0)

   def __str__(self):
        return self.admission_year

class PlacementFile(models.Model):
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE, related_name="placement")
    name = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    YEAR_CHOICES = [(str(r), str(r)) for r in range(2010, datetime.date.today().year+1)] 
    QUOTA_CHOICES = [('CET', 'CET'), ('MANAGEMENT', 'MANAGEMENT'), ('COMED-K', 'COMED-K'), ('SNQ', 'SNQ'), ('DIPLOMA', 'DIPLOMA')]
    PLACEMENT_CHOICES = [('ON_CAMPUS', 'ON_CAMPUS'), ('OFF_CAMPUS', 'OFF_CAMPUS'), ('INTERNSHIP', 'INTERNSHIP')]
    usn = models.CharField(max_length=255)
    admission_year = models.CharField(max_length=255, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    admission_quota = models.CharField(max_length=255, choices=QUOTA_CHOICES) 
    placement = models.CharField(max_length=255, choices=PLACEMENT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.usn

class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class StudentResult(models.Model):
    GRADE_CHOICES = [('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('PP', 'PP'), ('NP', 'NP')]
    SEM_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), ('7','7'), ('8', '8'), ('SUMMER 1 YEAR', 'SUMMER 1 YEAR'), ('SUMMER 2 YEAR', 'SUMMER 2 YEAR'), ('SUMMER 3 YEAR', 'SUMMER 3 YEAR'), ('SUMMER 4 YEAR', 'SUMMER 4 YEAR')]
    usn = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='result_usn', default=1)
    sem = models.CharField(max_length=255, choices=SEM_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    grade = models.CharField(max_length=255, choices=GRADE_CHOICES)

    def __str__(self):
        return self.grade









