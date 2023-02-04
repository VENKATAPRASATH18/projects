# from geopy.geocoders import Nominatim
# import folium
# def find(loc: str):
#     geolocator = Nominatim(user_agent="http")
#     location = geolocator.geocode(loc)
#     lat=location.latitude
#     long=location.longitude
#     list = str(location.address).split(',')
#     print(str(list).replace(","," "))
#     map=folium.Map(location=[lat,long])
#     map.show_in_browser

# loc="chennai central station"
# find(loc)
from geopy.geocoders import Nominatim

def find(loc: str):
    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(loc,timeout=None)
    lat = location.latitude
    long = location.longitude
    list = str(location.address).split(",")
    print(lat,long)


find("Himachal pradesh")
