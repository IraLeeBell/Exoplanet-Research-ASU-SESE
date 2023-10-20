import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

# Read the data from the text file
df = pd.read_csv('NormalizedFlux_HAT-P-28 b_2023-10-14.txt')

# Extract time (BJD) and normalized flux columns
time = df['BJD'].values
flux = df['Norm Flux'].values

# Plot flux over time
plt.figure(figsize=(10, 5))
plt.plot(time, flux, 'o-')
plt.xlabel('BJD')
plt.ylabel('Normalized Flux')
plt.title('HAT-P-28 - Flux over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate the Lomb-Scargle periodogram
frequency, power = LombScargle(time, flux).autopower(minimum_frequency=0.1, maximum_frequency=10)

# Plot the periodogram
plt.figure(figsize=(10, 5))
plt.plot(frequency, power)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('HAT-P-28 Lomb-Scargle Periodogram')
plt.grid(True)
plt.tight_layout()
plt.show()

# Identify the frequency of the highest peak (strongest periodic signal)
best_frequency = frequency[np.argmax(power)]
print(f"The most prominent frequency is: {best_frequency:.4f}")
print(f"This corresponds to a period of {1/best_frequency:.4f} days.")
