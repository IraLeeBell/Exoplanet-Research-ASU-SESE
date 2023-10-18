import os
from astropy.io import fits

def find_fits_with_jd(directory_path, target_jd):
    # Get all files in the specified directory
    files = os.listdir(directory_path)

    # Flag to indicate if a matching file was found
    found = False

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

                    # If target_jd is a whole number, match the integer parts
                    # Else, match exactly with a small threshold
                    if target_jd.is_integer():
                        if int(jd) == int(target_jd):
                            print(f"Found matching JD ({jd}) in file: {file_name}")
                            found = True
                    else:
                        if abs(jd - target_jd) < 1e-10:  # Small threshold for floating point imprecision
                            print(f"Found exact matching JD ({jd}) in file: {file_name}")
                            found = True

    # If no match was found, print a message
    if not found:
        print("No file match found for the specified JD.")

if __name__ == "__main__":
    # Specify the directory containing the FITS files
    directory = input("Enter the directory path (or press Enter for current directory): ")
    if not directory:
        directory = os.getcwd()
    
    # Get the target JD from the user
    target_jd_value = float(input("Enter the target JD value: "))
    
    # Search for the FITS files containing a matching JD
    find_fits_with_jd(directory, target_jd_value)
