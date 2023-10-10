%%time

import os
import re
import shutil

from ipywidgets import widgets, IntProgress, HBox, Label

from IPython.display import display, Image

from astropy.io import fits
from astropy.visualization import LogStretch, LinearStretch, HistEqStretch
from astropy.visualization.mpl_normalize import ImageNormalize

import matplotlib.pyplot as plt

# Progress bar
def initialize_progress_bar(max_count):
    progress = IntProgress(value=0, min=0, max=max_count, step=1, description='Loading:')
    label = Label('Ensuring images are loaded...')
    box = HBox([progress, label])
    display(box)
    return progress, label

def increment_progress(progress, label, step=1, description=None):
    progress.value += step
    if description:
        label.value = description

# Move bad image
def move_bad_image(file_path):
    bad_images = os.path.join(input_directory, "Bad Images")
    if not os.path.exists(bad_images):
        os.makedirs(bad_images)
        print("Bad Images folder created.")
    new_path = os.path.join(bad_images, os.path.basename(file_path))
    shutil.move(file_path, new_path)
    print("Image has been moved to Bad Images folder.")
    return new_path

# Undo the move of bad image
def undo_move_bad_image(file_path, original_path):
    if os.path.exists(file_path):
        shutil.move(file_path, original_path)
        print("Image has been moved back to the original folder.")
    else:
        print("Error: Image not found in the Bad Images folder.")

# fits images
def display_fits_image(file_path, stretch_type, intensity=1.0):
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        
    if stretch_type == "log":
        norm = ImageNormalize(data, stretch=LogStretch(a=intensity))
    elif stretch_type == "lin":
        norm = ImageNormalize(data, stretch=LinearStretch(a=intensity))
    elif stretch_type == "hist":
        norm = ImageNormalize(data, stretch=HistEqStretch(data))
    else:
        raise ValueError("Invalid stretch type")
    
    plt.imshow(data, cmap='gray', norm=norm)
    plt.colorbar()
    plt.show()
    
def display_fits_image_log(file_path):
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        
    # Applying the logarithmic stretch
    norm = ImageNormalize(data, stretch=LinearStretch())

    plt.imshow(data, cmap='gray', norm=norm)
    plt.colorbar()
    plt.show()

def display_fits_image_linear(file_path):
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        
    # Applying the linear stretch
    norm = ImageNormalize(data, stretch=LinearStretch())

    plt.imshow(data, cmap='gray', norm=norm)
    plt.colorbar()
    plt.show()

def display_fits_image_hist_eq(file_path):
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        
    # Applying the histogram equalization stretch
    norm = ImageNormalize(data, stretch=HistEqStretch(data))

    plt.imshow(data, cmap='gray', norm=norm)
    plt.colorbar()
    plt.show()

# Button callback
def on_button_click(button, file_path, image_num):
    move_bad_image(file_path)
    button.description = f"Image {image_num} Removed"
    button.button_style = 'danger'

input_directory = './images/'

if not os.path.exists(input_directory):
    print(f"Directory {input_directory} does not exist.")
    exit()

sorted_files = sorted(os.listdir(input_directory))
fits_files = [f for f in sorted_files if re.search(r"\.f[itz]+s?\.?g?z?$", f, re.IGNORECASE)]
json_files = [f for f in sorted_files if f.endswith('.json')]

print(f"Found {len(fits_files)} .FITS files and {len(json_files)} JSON files.")

# Prompt user to select how many images they want to evaluate
image_count = len(fits_files)
try:
    n = int(input(f"Enter a number between 1 and {image_count} for how many images you'd like to evaluate: "))
    if n < 1 or n > image_count:
        print(f"Please enter a number between 1 and {image_count}")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

selected_files = fits_files[:n]
progress, label = initialize_progress_bar(len(selected_files))

# Ask user for stretch type
stretch_options = ["log", "lin", "hist"]
stretch_type = input(f"Choose a stretch type ({'/'.join(stretch_options)}): ").lower()
if stretch_type not in stretch_options:
    print(f"Invalid stretch type. Please choose one of {', '.join(stretch_options)}.")
    exit()

# For LogStretch and LinearStretch, prompt the user for an intensity.
intensity = 1.0
if stretch_type in ["log", "lin"]:
    try:
        intensity = float(input(f"Enter the intensity for {stretch_type}Stretch (e.g., 1.0, 10.0, 100.0, 200.0, etc.): "))
        if intensity <= 0:
            print("Intensity should be a positive number.")
            exit()
    except ValueError:
        print("Invalid intensity value. Please enter a positive number.")
        exit()

for idx, file_name in enumerate(selected_files, start=1):
    increment_progress(progress, label, description=f"Loading image {idx}/{n}")
    file_path = os.path.join(input_directory, file_name)
    print(f"\n\n{idx}. {file_name}")
    display_fits_image(file_path, stretch_type, intensity)

    remove_button = widgets.Button(description=f'Remove Image {idx}')
    remove_button.button_style='success'
    
    undo_button = widgets.Button(description=f"Undo Remove {idx}", disabled=True)
    undo_button.file_path_in_bad = None  # Initialize here
    undo_button.original_path = file_path

    def create_remove_callback(button, undo_button, file_path, image_num):
        def callback(b):
            new_path = move_bad_image(file_path)
            button.description = f"Image {image_num} Removed"
            button.button_style = 'danger'
            undo_button.file_path_in_bad = new_path
            undo_button.disabled = False
        return callback

    remove_button.on_click(create_remove_callback(remove_button, undo_button, file_path, idx))

    def create_undo_callback(undo_button):
        def callback(b):
            if undo_button.file_path_in_bad and undo_button.original_path:
                undo_move_bad_image(undo_button.file_path_in_bad, undo_button.original_path)
                remove_button.description = f'Remove Image {idx}'
                remove_button.button_style = 'success'
                b.disabled = True
        return callback

    undo_button.on_click(create_undo_callback(undo_button))
    
    display(widgets.HBox([remove_button, undo_button]))