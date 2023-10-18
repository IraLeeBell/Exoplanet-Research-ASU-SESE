import os
from astropy.io import fits

def find_closest_jd_file(directory_path, target_jd, uncertainty):
    # Get all files in the specified directory
    files = os.listdir(directory_path)

    closest_jd_difference = float('inf')  # Set initial difference to infinity
    closest_jd_file = None
    closest_jd_value = None

    # Loop through all files
    for file_name in files:
        # Check if the file has a .fits extension (case insensitive)
        if file_name.lower().endswith('.fit'):
            # Construct the full path to the file
            file_path = os.path.join(directory_path, file_name)
            
            # Open the FITS file and extract JD value
            with fits.open(file_path) as hdul:
                header = hdul[0].header
                if 'JD' in header:
                    jd = header['JD']

                    # Calculate difference between target JD and current JD
                    jd_difference = abs(jd - target_jd)

                    # Update closest JD values if the current JD is closer
                    if jd_difference < closest_jd_difference:
                        closest_jd_difference = jd_difference
                        closest_jd_file = file_name
                        closest_jd_value = jd

    # If the closest JD is within the specified uncertainty range, print it
    if closest_jd_difference <= uncertainty:
        print(f"Closest JD ({closest_jd_value}) found in file: {closest_jd_file}")
    else:
        print("No file found within the specified uncertainty range.")

if __name__ == "__main__":
    # Specify the directory containing the FITS files
    directory = input("Enter the directory path (or press Enter for current directory): ")
    if not directory:
        directory = os.getcwd()
    
    # Get the target JD (Mid-transit time) from the user
    target_jd_value = float(input("Enter the Mid-transit time (JD value): "))
    
    uncertainty_value = float(input("Enter the uncertainty: +/- "))

    # Find the FITS file with the closest JD value
    find_closest_jd_file(directory, target_jd_value, uncertainty_value)



