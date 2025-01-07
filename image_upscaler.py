import os
from PIL import Image

def upscale_image(image_path, save_path, target_mp=4):
    """
    Upscales an image to meet the target megapixels (minimum 4 MP).
    
    :param image_path: Path to the original image.
    :param save_path: Path to save the upscaled image.
    :param target_mp: Target megapixels (default 4 MP).
    """
    with Image.open(image_path) as img:
        width, height = img.size
        current_mp = (width * height) / 1e6
        
        if current_mp >= target_mp:
            print(f"Image already meets requirements: {image_path} ({current_mp:.2f} MP)")
            return  # No need to upscale
        
        # Calculate scaling factor
        scale_factor = (target_mp / current_mp) ** 0.5
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        
        # Resize the image using LANCZOS resampling filter
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img_resized.save(save_path)
        print(f"Upscaled {image_path} to {new_width}x{new_height} ({target_mp} MP) and saved to {save_path}")

def process_folder(folder_path, target_mp=4):
    """
    Processes a folder of images, upscales images below the target megapixels, and saves them in a new folder.
    
    :param folder_path: Path to the folder containing images.
    :param target_mp: Target megapixels (default 4 MP).
    """
    # Create a new folder in the same directory as the original folder
    parent_dir = os.path.dirname(folder_path)
    folder_name = os.path.basename(folder_path)
    output_folder = os.path.join(parent_dir, f"{folder_name}_processed")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(f"Saving upscaled images to: {output_folder}")
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        save_path = os.path.join(output_folder, filename)
        
        try:
            upscale_image(file_path, save_path, target_mp=target_mp)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing images: ").strip().strip('"')
    target_mp = 4  # Minimum required megapixels for Adobe Stock

    process_folder(folder_path, target_mp=target_mp)
