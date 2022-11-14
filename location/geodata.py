from django.utils.translation import ugettext as _
import json
from location.models import Country, Province, City

#Getting data from json files
with open('json_data/countries_data.json') as file:
    cdata = json.load(file)

with open('json_data/provinces_data.json') as file:
    pdata = json.load(file)

with open('json_data/cities_data.json') as file:
    rdata = json.load(file)


#Iterating through data obtained from json files
for country in cdata:
    country_object = Country.objects.create(
			name=country['name'],
			code=country['code']
          )

    country_provinces=list(filter(lambda province: province['country']==country['code'], pdata))
    
    for province in country_provinces:
        province_object = Province.objects.create(
            name=province['name'],
            country=country_object
        )
        
        province_cities=list(filter(lambda city: city['provinceId']==province['id'], rdata))
        
        for city in province_cities:
            city_object = City.objects.create(
                name=city['name'],
                country=country_object,
                province=province_object
            )