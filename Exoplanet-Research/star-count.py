from astropy.io import fits

def inspect_fits_file(file_path):
    # Open the FITS file
    with fits.open(file_path) as hdul:
        
        # Print basic information about the FITS file
        hdul.info()
        
        # Attempt to locate and analyze the table with star detections
        for hdu in hdul:
            if isinstance(hdu, fits.BinTableHDU) or isinstance(hdu, fits.TableHDU):
                data = hdu.data
                print("\nDetected a table. Columns are:")
                print(data.columns)
                
                # Assuming 'X' and 'Y' are the column names for star coordinates
                if 'X' in data.columns.names and 'Y' in data.columns.names:
                    x_coords = data['X']
                    y_coords = data['Y']
                    print(f"\nTotal number of stars detected: {len(x_coords)}")
                    
                    # Print the coordinates of the detected stars
                    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
                        print(f"Star {i+1} detected at coordinates: X={x}, Y={y}")
                break

file_path = input("Enter the path to the FITS file: ")
inspect_fits_file(file_path)
