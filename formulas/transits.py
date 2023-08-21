import math

# Calculate Area
def area(x=0):
	radius = x

	return math.pi * (radius ** 2)

result = area(10)
print(f'The area of the planet or star is {result}.')


# Brightness Drop = Brightness Before Transit - Brightness During Transit
def brightness_drop(x=0, y=1):
	brightness_before_transit = x
	brightness_during_transit = y

	return brightness_before_transit - brightness_during_transit

result = brightness_drop(40,30)
print(f'The Brightness Drop is {result}')


# % Brightness Drop = ((Brightness Before Transit - Brightness During Transit)/Brightness Before Transit) * 100%
def percent_brightness_drop(x=0, y=1):
	brightness_before_transit = x
	brightness_during_transit = y

	return ((brightness_before_transit/brightness_during_transit)/brightness_during_transit) * 100

result = percent_brightness_drop(20,30)
print(f'The Brightness Drop using brightness before transit and brightness during transit is {result}%')

# % Brightness Drop = ((Star Area - Planet Area)/Star Area) * 100%
def percent_brightness_drop_area(x=0, y=1):
	star_area = x
	planet_area = y

	return (planet_area/star_area) * 100

result = percent_brightness_drop_area(10000000,30)
print(f'The Brightness Drop using the star and planet area is {result}%')

# % Brightness Drop using Radius of Star and Planet
def percent_brightness_drop_radius(x=0, y=1):
	radius_star = x
	radius_planet = y

	area_star = math.pi * (radius_star ** 2)
	area_planet = math.pi * (radius_planet ** 2)

	return (area_planet/area_star) * 100

result = percent_brightness_drop_radius(100000,34)
print(f'The Brightness Drop usiing the radius of a star and the radius of a planet is {result}%.')
