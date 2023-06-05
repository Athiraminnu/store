from django.db import models

# Create your models here.


class ClgStore(models.Model):
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    image = models.ImageField(upload_to="dep")
    dep_name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.dep_name
