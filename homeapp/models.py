from django.db import models

class Card_Model(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    job_title = models.CharField(max_length=50)
    last_date = models.DateField()
    location = models.CharField(max_length=50)
    apply_link = models.CharField(max_length=500)

    def __str__(self):
        return self.company_name