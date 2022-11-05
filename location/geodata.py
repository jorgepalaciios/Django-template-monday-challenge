import json
from models import Country, Province, City

with open('json_data/countries_data.json') as file:
    data = json.load(file)


# def get_country_data(self, data):
#     for country in data['name']['code']:
#         get_countryname = country['name'],
#         get_countrycode = country['code']

#im trying to figure out things up here, to catch them down
#and then create the instances need it for django
#to generate the data for the db

# def generate_country(count):
# 	for country in range(count):
# 		country_name = get_countryname() # i think i should replace this with another logic 
# 		country_code = generate_countrycode()

# 		Country.objects.create(
# 			name=country_name,
# 			code=country_code
# )