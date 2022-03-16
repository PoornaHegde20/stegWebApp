from django.db import models

# Create your models here.
class lsbEncoding(models.Model):
    id=models.AutoField(primary_key=True)
    inputImageName=models.CharField(max_length=100)
    inputImagePath=models.FileField(upload_to='media/images/', null=True, verbose_name="")
    text=models.TextField(max_length=250)
    outputImageName=models.CharField(max_length=100)
    outputImagePath=models.FileField(upload_to='media/images/', null=True, verbose_name="")
    def __str__(self):
        return self.inputImageName


class lsbDecoding(models.Model):
    id=models.AutoField(primary_key=True)
    inputImageName=models.CharField(max_length=100)
    inputImagePath=models.FileField(upload_to='media/images/', null=True, verbose_name="")
    text=models.TextField(max_length=250)
    def __str__(self):
        return self.inputImageName

    

    