# % Brightness Drop = ((Brightness Before Transit - Brightness During Transit)/Brightness Before Transit) * 100%

def percent_brightness_drop(x=0, y=1):
	brightness_before_transit = x
	brightness_during_transit = y

	return ((brightness_before_transit/brightness_during_transit)/brightness_during_transit) * 100

result = percent_brightness_drop(20,30)
print(result)
