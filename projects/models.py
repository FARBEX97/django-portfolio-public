from django.db import models


# Create your models here.
class CodeProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    demo_link = models.CharField(max_length=300,blank=True)
    repo_link = models.CharField(max_length=300,blank=True)

    class Meta:
        verbose_name = 'Code project'
        verbose_name_plural = 'Code projects'

    def __str__(self):
        return self.name
