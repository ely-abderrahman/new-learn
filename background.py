import keyboard
import ctypes
import os
import glob
import time

# Constants
SPI_SETDESKWALLPAPER = 20

# Function to change the desktop background
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Specify the path to the directory containing your images
image_directory = "C:\\Users\\HP\\OneDrive\\Pictures\\wallpaper"

# Get a list of all image files in the directory
image_paths = glob.glob(os.path.join(image_directory, "*.jpg"))

# Variable to track the current index
current_index = 0

# Variable to track whether the script is paused
is_paused = False

# Function to toggle the desktop background
def toggle_wallpaper():
    global current_index
    if not is_paused and image_paths:
        current_index = (current_index + 1) % len(image_paths)
        set_wallpaper(image_paths[current_index])

# Function to pause or resume the script
def pause_resume():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        print("Script paused. Press ° again to resume.")
    else:
        print("Script resumed.")

# Register the § key event handler to toggle wallpaper
keyboard.add_hotkey('§', toggle_wallpaper)

# Register the ° key event handler to pause/resume the script
keyboard.add_hotkey('°', pause_resume)

# Keep the script running indefinitely
keyboard.wait()
