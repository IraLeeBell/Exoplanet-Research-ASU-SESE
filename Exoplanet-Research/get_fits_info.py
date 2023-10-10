from astropy.io import fits

def print_fits_contents(filename):
    # Open the FITS file
    with fits.open(filename) as hdul:
        # Loop over each Header Data Unit (HDU) in the FITS file
        for hdu in hdul:
            # Print the header information
            print("Header:")
            print(repr(hdu.header))
            
            # If the HDU contains data, print it
            if hdu.data is not None:
                print("Data:")
                print(hdu.data)

if __name__ == "__main__":
    print_fits_contents("lrgb-min-10-0007lum-1-60.fit")
