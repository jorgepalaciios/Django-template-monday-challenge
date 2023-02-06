from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField( max_length=200, unique=True)
    code = models.CharField( max_length=10, unique=True)

    class Meta:
        db_table = 'countries'
    def __str__(self):
        return self.name
    

class Province(models.Model):
    name = models.CharField( max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'provinces'
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField( max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name