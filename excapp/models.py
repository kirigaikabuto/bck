from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataHistory(models.Model):
    parent = models.ForeignKey(Data, related_name="parent", on_delete=models.CASCADE)
    child = models.ForeignKey(Data, related_name="child", on_delete=models.CASCADE)

    def __str__(self):
        return self.parent.name + "->" + self.child.name
