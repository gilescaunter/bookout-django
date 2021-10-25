from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Logsheet(models.Model):
    pilot = models.CharField(max_length=255)
    logDate = models.DateField()
    logTime = models.CharField(max_length=5)
    logFrom = models.CharField(max_length=30)
    logTo = models.CharField(max_length=30)
    logAircraftType = models.CharField(max_length=20)
    logAircraftReg = models.CharField(max_length=20)
    logPax = models.IntegerField(default=1)
    logDorA = models.CharField(max_length=1)
    logEntryDatetime = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
#    created_by = models.ForeignKey(User, related_name='+')
#    updated_by = models.ForeignKey(User, null=True, related_name='+')
    def __str__(self):
        return self.pilot


class Pilots(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    aircraftType = models.CharField(max_length=20)
    aircraftReg = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
#    created_by = models.ForeignKey(User, related_name='+')
#    updated_by = models.ForeignKey(User, null=True, related_name='+')
    def __str__(self):
        return self.firstName

