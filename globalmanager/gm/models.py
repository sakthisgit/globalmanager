from django.db import models

# Create your models here.

class GmData(models.Model):
    gm_name = models.CharField(max_length=50)

    def __str__(self):
        return self.gm_name

class GmValue(models.Model):
    category = models.ForeignKey(GmData, on_delete=models.CASCADE)
    category_value=models.CharField(max_length=50)

    def __str__(self):
        return self.category_value



    
