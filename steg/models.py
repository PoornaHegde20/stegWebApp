from django.db import models

# Create your models here.


class LSBEncode(models.Model):
    id = models.AutoField(primary_key=True)
    inputImagePath = models.FileField(
        upload_to='images/', null=False, verbose_name="")
    outputImagePath = models.FileField(
        upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return str(self.inputImagePath) + " ID : " + str(self.id)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('steg:show_img', kwargs={'id': self.id})


class LSBDecode(models.Model):
    id = models.AutoField(primary_key=True)
    inputImagePath = models.FileField(
        upload_to='images/', null=True, verbose_name="")
    message = models.TextField(max_length=1000, default="")

    def __str__(self):
        return str(self.inputImagePath)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('steg:show_img_decode', kwargs={'id': self.id})
