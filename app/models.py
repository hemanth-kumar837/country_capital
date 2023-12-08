from django.db import models

# Create your models here.
class Country(models.Model):
    Country_name=models.CharField(max_length=50 , primary_key=True)
    def __str__(self):
        return self.Country_name

class Capital(models.Model):
    Country_name=models.OneToOneField(Country, on_delete=models.CASCADE)
    capital=models.CharField(max_length=50)
    def __str__(self):
        return self.capital