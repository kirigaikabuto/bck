from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=255)
    file=models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)