from django.db import models
from tinymce.models import  HTMLField

# Create your models here.
class  views(models.Model):
    gtitle=models.CharField(max_length=200)
    gcontext=HTMLField(max_length=1000)
    gpic=models.ImageField()
    #def __str__(self):
     #   return self.gtitle.encode('utf-8')

class YcListViews(models.Model):
    gtitle = models.CharField(max_length=20)
    gcontext = models.TextField()
    gpic = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'yc_list_views'

