from pyexpat import model
from django.db import models
from django.forms import IntegerField
# from tinymce.models import HTMLField

class Card_Model(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    slug = models.CharField(max_length=50, blank=False, unique=True)
    position = models.CharField(max_length=50, blank=True)
    salary = models.CharField(max_length=50, blank=True, default='Not Disclosed')
    batch = models.CharField(max_length=50, blank=True, default='Any Batch')
    degree = models.CharField(max_length=50, blank=True , default='Not Disclosed')
    last_date = models.CharField(max_length=50, blank=True, default='Not Disclosed')
    location = models.CharField(max_length=50, blank=True, default='PAN India')


    def __str__(self):
        return self.company_name


class Blog_Model(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    slug = models.CharField(max_length=50, blank=False, unique=True)
    content = models.TextField()
    Skill_des = models.TextField()
    min_qulification = models.TextField()
    how_to_apply = models.TextField()
    link = models.URLField(max_length=200, null = True)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.company_name

