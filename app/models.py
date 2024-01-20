from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100,primary_key=True)
    country_code = models.PositiveIntegerField()
    def __str__(self):
        return self.country_name
    
class Capital(models.Model):
    country_name = models.OneToOneField(Country,on_delete=models.CASCADE)
    capital_name = models.CharField(max_length=100)

    def __str__(self):
        return self.capital_name
    
    
