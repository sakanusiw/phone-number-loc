import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Taking input of the phone number along with the country code
number = input("Enter the PhoneNumber with the country code: ")

# Parsing the phone number string to convert it into phone number format
phoneNumber = phonenumbers.parse(number, None)

# Storing the API Key in the Key variable
Key = "e9d8f31fe6c044369f99281c1853f80e"  # Generate your API key at https://opencagedata.com/api

# Using the geocoder module of phonenumbers to get the location in console
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + yourLocation)

# Using the carrier module of phonenumbers to get the service provider name in console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Service Provider: " + yourServiceProvider)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)

# Getting the map for the given location
query = str(yourLocation)
results = geocoder.geocode(query)

# Extracting latitude and longitude values
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Reverse geocoding to get a more specific address
reverse_results = geocoder.reverse_geocode(lat, lng)
address = reverse_results[0]['formatted']

# Getting the map for the given latitude and longitude
myMap = folium.Map(location=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=address).add_to(myMap)

# Save the map to an HTML file to open it and see the actual location in map format
myMap.save("Location.html")
