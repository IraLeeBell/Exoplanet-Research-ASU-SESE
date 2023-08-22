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

# Determine size of planet from % of brightness drop using absolute values
def size_of_planet_from_brightness_drop(x=0,y=1):
	varBrightnessDrop = x
	varRadiusOfStar = y

	return math.sqrt(varBrightnessDrop/100) * varRadiusOfStar

result = size_of_planet_from_brightness_drop(88, 10000000)
print(f'The size of the planet using the % brightness drop and the radius of a star is {result}.')

# Using big R and little R we can talk about sizes relative to Earth and the Sun
# Rplanet = rplanet/rEarth
# Rstar = rstar/rSun
# rplanet = Rplanet x rEarth
# rstar = Rstar * rSun

# Determine the size of a planet from % Brightness Drop using relative sizes
def size_of_planet_using_relative_sizes(x=0,y=1):
	R_star = x
	varPercentBrightnessDrop = y

	return (math.sqrt(varPercentBrightnessDrop/100)) * R_star * 109

result = size_of_planet_using_relative_sizes(50, 5)
print(f'The relative size of the planet using the % Brightness Drop and the relative size of the Star to our Sun is {result}.')

