import json
#from .models import Country, Province, City

with open('json_data/countries_data.json') as file:
    cdata = json.load(file)
with open('json_data/cities_data.json') as file:
    rdata = json.load(file)


for country in cdata:
    country_id = country['id'],
    country_name = country['name'],
    country_code = country['code'],


with open('json_data/provinces_data.json') as file:
    pdata = json.load(file)


for province in pdata:
    province_id = province['id'],
    province_name = province['name'],
    c_code = province['country']
    

# p=list(filter(lambda c_code: c_code==country_code), pdata)
# print(p)

for city in rdata:
    city_name = city['name'],
    c_id = city['countryId'],
    p_id = city['provinceId']




 
# list(filter(lambda p: country_code==country, province_data))


# def generate_country():
# 	for country in range(count):
# 		country_name = get_countryname() # i think i should replace this with another logic 
# 		country_code = generate_countrycode()

# 		Country.objects.create(
# 			name=country_name,
# 			code=country_code
#           ) 

# city_data_json file 
# {
#   "id": 1,
#   "name": "Agdam",
#   "provinceId": 1,
#   "countryId": 3
# },

# province_daja_json file

#  {
#     "id": 6,
#     "country": "BY",
#     "name": "Vitebskaya obl."
#   },

#im trying to figure out things up here, to catch them down
#and then create the instances need it for django
#to generate the data for the db

# 
# funcion filter*** create iteration inside to continue getting the data
#to the other 
# filter list of dictionaries (search)