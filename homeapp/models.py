from django.db import models


class Card_Model(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    position = models.CharField(max_length=50, blank=True)
    salary = models.CharField(max_length=50, blank=True, default='Not Disclosed')
    batch = models.CharField(max_length=50, blank=True, default='Any Batch')
    degree = models.CharField(max_length=50, blank=True , default='Not Disclosed')
    last_date = models.CharField(max_length=50, blank=True, default='Not Disclosed')
    location = models.CharField(max_length=50, blank=True, default='PAN India')
    apply_link = models.CharField(max_length=500)

    def __str__(self):
        return self.company_name
