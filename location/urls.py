from django.urls import path


# others
from .views import (
    CountryCreation,
    ProvinceCreation,
    CityCreation
)


app_name = 'location'

urlpatterns = [
    path('countries/creation/', CountryCreation.as_view(), name='countries_creation'),
    path('provinces/creation/', ProvinceCreation.as_view(), name='provinces_creation'),
    path('cities/creation/', CityCreation.as_view(), name='cities_creation'),
]