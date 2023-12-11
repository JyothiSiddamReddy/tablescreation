from django.db import models

# Create your models here.
 
class Country(models.Model):
    country_Id=models.IntegerField(primary_key=True)
    country_Name=models.CharField(max_length=150)

    def __str__(self):
        return self.country_Name
    


class Capital(models.Model):
    capital_Id=models.IntegerField(primary_key=True)
    capital_Name=models.CharField(max_length=100)
    country_Id=models.OneToOneField(Country,on_delete=models.CASCADE)


    def __str__(self):
        return self.capital_Name
    

