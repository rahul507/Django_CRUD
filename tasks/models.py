from django.db import models


# Create your models here.




class Task(models.Model):
    name = models.CharField(verbose_name="driver name", max_length=65)
    id_num = models.IntegerField(verbose_name="driver id number", unique=True,default=None)
    email = models.CharField(verbose_name="driver email", max_length=65, unique=True,default=None)
    phone = models.IntegerField(verbose_name="driver number",unique=True,default=None)
    password = models.CharField(verbose_name="driver Password", max_length=65, default='company123')
    

    def __str__(self):
        return self.name
