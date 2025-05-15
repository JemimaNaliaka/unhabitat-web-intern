import pandas as pd
from django.db import models
from django.db import migrations


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class OrgUnit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    start_date = models.DateField()
    end_date = models.DateField()
                            
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    org_unit = models.ForeignKey(OrgUnit, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def populate_country(apps, schema_editor):
    Country = apps.get_model('projects', 'Country')
    Country.objects.get_or_create(name="Kenya")
    Country.objects.get_or_create(name="Uganda")

class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0001_initial'),
            ]

    operations = [
        migrations.RunPython(populate_country),
                ]
