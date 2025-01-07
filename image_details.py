import os
from PIL import Image

def check_image_details(folder_path):
    """
    Checks and prints the resolution and megapixels of each image in the given folder.
    
    :param folder_path: Path to the folder containing images
    """
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print("The specified folder does not exist.")
        return

    print(f"Checking image details in folder: {folder_path}\n")
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process image files
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                megapixels = (width * height) / 1e6
                print(f"File: {filename}")
                print(f" - Dimensions: {width}x{height}")
                print(f" - Megapixels: {megapixels:.2f} MP\n")
        except Exception as e:
            print(f"Skipping file: {filename} (not a valid image). Error: {e}\n")

if __name__ == "__main__":
    # Ask user to provide folder path
    folder_path = input("Enter the path to the folder containing images: ").strip()
    check_image_details(folder_path)
