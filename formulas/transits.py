# Ira Bell
# Arizona State University
# School of Earth and Space Exploration
# Exoplanet Research - Fall 2023
# Transit Photometry

import math

# Calculate Area
def area(x=0):
	radius = x

	return math.pi * (radius ** 2)

result = area(10)
print(f'\nThe area of the planet or star is {result}.')


# Brightness Drop = Brightness Before Transit - Brightness During Transit
def brightness_drop(x=0, y=1):
	brightness_before_transit = x
	brightness_during_transit = y

	return brightness_before_transit - brightness_during_transit

result = brightness_drop(40,30)
print(f'\nThe Brightness Drop is {result}')


# % Brightness Drop = ((Brightness Before Transit - Brightness During Transit)/Brightness Before Transit) * 100%
def percent_brightness_drop(x=0, y=1):
	brightness_before_transit = x
	brightness_during_transit = y

	return ((brightness_before_transit/brightness_during_transit)/brightness_during_transit) * 100

result = percent_brightness_drop(20,30)
print(f'\nThe Brightness Drop using brightness before transit and brightness during transit is {result}%')

# % Brightness Drop = ((Star Area - Planet Area)/Star Area) * 100%
def percent_brightness_drop_area(x=0, y=1):
	star_area = x
	planet_area = y

	return (planet_area/star_area) * 100

result = percent_brightness_drop_area(10000000,30)
print(f'\nThe Brightness Drop using the star and planet area is {result}%')

# % Brightness Drop using Radius of Star and Planet
def percent_brightness_drop_radius(x=0, y=1):
	radius_star = x
	radius_planet = y

	area_star = math.pi * (radius_star ** 2)
	area_planet = math.pi * (radius_planet ** 2)

	return (area_planet/area_star) * 100

result = percent_brightness_drop_radius(100000,34)
print(f'\nThe Brightness Drop usiing the radius of a star and the radius of a planet is {result}%.')

# Determine size of planet from % of brightness drop using absolute values
def size_of_planet_from_brightness_drop(x=0,y=1):
	varBrightnessDrop = x
	varRadiusOfStar = y

	return math.sqrt(varBrightnessDrop/100) * varRadiusOfStar

result = size_of_planet_from_brightness_drop(88, 10000000)
print(f'\nThe size of the planet using the % brightness drop and the radius of a star is {result}.')

# Using big R and little R we can talk about sizes relative to Earth and the Sun
# Rplanet = rplanet/rEarth
# Rstar = rstar/rSun
# rplanet = Rplanet x rEarth
# rstar = Rstar * rSun

# Determine the size of a planet from % Brightness Drop using relative sizes when comparing to Earth
def size_of_planet_using_relative_sizes(x=0,y=1):
	R_star = x
	varPercentBrightnessDrop = y

	return (math.sqrt(varPercentBrightnessDrop/100)) * R_star * 109

result = size_of_planet_using_relative_sizes(50, 5)
print(f'\nThe relative size of the planet in comparison to Earth using the % Brightness Drop and the relative size of the Star to our Sun is {result}.')

# Determine the size of a planet from % Brightness Drop using relative sizes when comparing to Jupiter
def size_of_planet_using_relative_sizes(x=0,y=1):
	R_star = x
	varPercentBrightnessDrop = y

	return (math.sqrt(varPercentBrightnessDrop/100)) * R_star * 9.72

result = size_of_planet_using_relative_sizes(50, 5)
print(f'\nThe relative size of the planet in comparison to Jupiter using the % Brightness Drop and the relative size of the Star to our Sun is {result}.')


## This function is the most accurate for now.
def test_earth(x=0,y=1):
	test_earth_brightness_drop = x
	test_earth_radius_of_star = y

	earth_result = ((test_earth_brightness_drop/100) ** (1/2)) * test_earth_radius_of_star * 109

	jupter_result = earth_result * 0.0892

	return earth_result,jupter_result

result = test_earth(0.03, 10)
print(result)

# Kepler's Third Law
# period ** 2 = distance ** 3
# period = distance ** (3/2)
# period = distance ** 1.5
# distance ** 3 = (period ** 2) * star_mass
# distance = ((period ** 2) * star_mass)**(1/3)
# (period ** 2) * star_mass = distance ** 3

def find_distance_with_period_and_star_mass(x=0,y=0):
	period = x
	star_mass = y

	return ((period ** 2) * star_mass) ** (1/3)

result = find_distance_with_period_and_star_mass(0.0273972602739726, 0.7)
print(f'\nThe orbital radius/distance of the exoplanet using the period and star mass is {result}.')



