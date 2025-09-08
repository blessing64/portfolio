from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(default="sample.png", blank=True)
    
    
    def __str__(self):
        return f"{self.name}"