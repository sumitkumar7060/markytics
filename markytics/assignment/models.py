from django.db import models

# Create your models here.


class registration(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.user_name


class incident(models.Model):
    location = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    incident_location = models.CharField(max_length=250)
    severity = models.CharField(max_length=250)
    suspected_cause = models.CharField(max_length=250)
    action = models.CharField(max_length=250)
    sub_incident = models.CharField(max_length=250)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.user
