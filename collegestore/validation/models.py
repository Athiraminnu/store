from django.db import models

# Create your models here.


class Dpt(models.Model):
    dpt_id = models.IntegerField(primary_key=True)
    d_name = models.CharField(max_length=100)

    def __str__(self):
        return self.d_name


class Course(models.Model):
    dpt_id = models.IntegerField()
    c_name = models.CharField(max_length=100)
    c_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.c_name
