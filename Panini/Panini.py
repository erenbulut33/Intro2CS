city = ("Poznan", "Poland", 52.41, 16.93)
print("Name of the country is:")
print(city[1])
print("Latitude of the city is:")
print(city[-1])
print(type(city))

# Unpacking the tuple
city_name, country, latitude, longitude = city

print(city_name)
print(country)


city_list = list(city)
city_list[1] = "Hungary"
city_updated = tuple(city_list)

print(city_updated)