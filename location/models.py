from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField( max_length=50, unique=True)
    code = models.CharField( max_length=10, unique=True)

    class Meta:
        db_table = 'countries'

class Province(models.Model):
    name = models.CharField( max_length=50)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'provinces'

class City(models.Model):
    name = models.CharField( max_length=50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'