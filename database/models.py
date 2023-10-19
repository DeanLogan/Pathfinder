from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User

class Pathway(models.Model):
    pathwayID = models.CharField(primary_key=True,max_length=4, auto_created=False)
    pathwayName = models.CharField(max_length=100)
    pathwayLevels = models.IntegerField(default=3)
    def __str__(self):
        return self.pathwayID

class Module(models.Model):
    moduleID = models.CharField(primary_key=True ,max_length=7, auto_created=False)
    moduleName = models.CharField(max_length=100)
    moduleSemester = models.IntegerField(default=3)
    moduleDescription = models.CharField(max_length=2500)
    moduleLevel = models.IntegerField(default=1)
    moduleWeight = models.IntegerField(default=20)
    def __str__(self):
        return self.moduleID
    
class Lecturer(models.Model):
    lecturerID = models.IntegerField(primary_key=True, auto_created=True)
    lecturerName = models.CharField(max_length=100)
    lecturerEmail = models.EmailField()
    lecturerModules = models.ManyToManyField(Module)
    def __str__(self):
        return str(self.lecturerID)
    
class Assessment(models.Model):
    assessmentID = models.CharField(primary_key=True, auto_created=True, max_length=8)
    moduleID = models.ForeignKey(Module, on_delete=models.CASCADE)
    assessmentType = models.CharField(max_length=20)
    assessmentWeight = models.FloatField(default=20)
    def __str__(self):
        return str(self.assessmentID)

class ModulePathway(models.Model):
    modulePathwayID = models.IntegerField(primary_key=True, auto_created=True)
    moduleID = models.ForeignKey(Module, on_delete=models.CASCADE)
    pathwayID = models.ForeignKey(Pathway, on_delete=models.CASCADE)
    mpCore = models.BooleanField(default=True) # either optional or core
    def __str__(self):
        return str(self.modulePathwayID)
    
class Student(models.Model):
    studentID = models.IntegerField(primary_key=True, auto_created=False)
    pathwayID = models.ForeignKey(Pathway, on_delete=models.SET_NULL, null=True)
    studentCurrentLevel = models.IntegerField(default=1)
    studentCurrentSemester = models.IntegerField(default=1)
    currentPathwayMark = models.FloatField(default=0, editable=False)
    def __str__(self):
        return str(self.studentID)

class StudentModule(models.Model):
    studentModuleID = models.IntegerField(primary_key=True, auto_created=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    moduleID = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    stuModMark = models.FloatField(default=0, editable=False)
    def __str__(self):
        return str(self.studentModuleID)

class StudentInterest(models.Model):
    studentInterestID = models.IntegerField(primary_key=True, auto_created=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    interestName = models.CharField(max_length=100)
    interestImportance = models.IntegerField(default=0)
    def __str__(self):
        return str(self.studentInterestID)
    
class StudentModuleAssessment(models.Model):
    studentModuleAssessmentID =  models.IntegerField(primary_key=True, auto_created=True)
    studentModuleID = models.ForeignKey(StudentModule, on_delete=models.CASCADE)
    assessmentID = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    assessmentMark = models.FloatField(default=100)

