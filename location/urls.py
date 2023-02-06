from django.urls import path, include
from rest_framework.routers import DefaultRouter
# others
from . import views


app_name = 'location'


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename="countries")
router.register(r'provinces', views.ProvinceViewSet, basename="provinces")
router.register(r'cities', views.CityViewSet, basename="cities")


urlpatterns = [
    path('', include(router.urls)),
    
]