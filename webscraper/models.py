from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
