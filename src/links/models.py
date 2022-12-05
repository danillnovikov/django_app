from django.db import models

# Create your models here.

class Links(models.Model):
    # id/pk - pk int - auto
    name = models.CharField(
        verbose_name="Video's name",
        max_length=100)
    links = models.URLField(
        null=False
    )
    
    def __str__(self): 
        return self.name