import os
from PIL import Image

def resize_images_in_folder(folder_path, target_size=(224, 224)):
    """
    Resize all images in a folder and its subfolders to the specified target size.
    
    Args:
        folder_path (str): Path to the folder containing images.
        target_size (tuple): Target size of the images in the format (width, height).
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        resized_img = img.resize(target_size)
                        resized_img.save(image_path)
                        print(f"Resized {image_path} to {target_size}")
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

# Example usage
folder_path = r"C:\Users\vjhjh\Downloads\fruitsetlegumes-20240522T012543Z-001\fruitsetlegumes"
resize_images_in_folder(folder_path)
