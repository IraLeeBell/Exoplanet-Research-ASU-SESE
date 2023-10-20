import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

# Load the FITS file
file_path = 'lum-bin-2-min-15-0049lum-2-60.fit'
hdul = fits.open(file_path)

# Extract the data from the primary HDU (index 0)
data = hdul[0].data

# Print some basic statistics
print(f"Mean ADU: {np.mean(data):.2f}")
print(f"Median ADU: {np.median(data):.2f}")
print(f"Standard Deviation: {np.std(data):.2f}")
print(f"Max ADU: {np.max(data)}")
print(f"Min ADU: {np.min(data)}")

# Optionally, visualize the data with a histogram
plt.hist(data.flatten(), bins=100, log=True)
plt.xlabel('ADU')
plt.ylabel('Number of Pixels')
plt.title('Histogram of ADU values')
plt.show()

# Close the FITS file
hdul.close()
