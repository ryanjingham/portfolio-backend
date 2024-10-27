from django.db import models

# Create your models here.


class StackItem(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ExperienceItem(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=100, null=True, blank=True)
    stack = models.ManyToManyField(StackItem, related_name='portfolio_items')
    link = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.title

    