from PIL import Image, ImageOps
import os

def augment_images(input_directory, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Get list of all files in the input directory
    files = os.listdir(input_directory)
    
    # Filter out only image files (assuming jpg and png for this example)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    for filename in image_files:
        # Open an image file
        img_path = os.path.join(input_directory, filename)
        with Image.open(img_path) as img:
            # Rotate the image 90, 180, and 270 degrees
            for angle in [90, 180, 270]:
                rotated_img = img.rotate(angle)
                rotated_filename = f"{os.path.splitext(filename)[0]}_rotated_{angle}{os.path.splitext(filename)[1]}"
                rotated_img.save(os.path.join(output_directory, rotated_filename))
                print(f"Saved rotated image: {rotated_filename}")
            
            # Flip the image horizontally
            flipped_img = ImageOps.mirror(img)
            flipped_filename = f"{os.path.splitext(filename)[0]}_flipped{os.path.splitext(filename)[1]}"
            flipped_img.save(os.path.join(output_directory, flipped_filename))
            print(f"Saved flipped image: {flipped_filename}")
            
            # Zoom in and out (for simplicity, we'll just resize to 150% and 50%)
            for scale, suffix in [(1.5, 'zoomed_in'), (0.5, 'zoomed_out')]:
                width, height = img.size
                zoomed_img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
                zoomed_filename = f"{os.path.splitext(filename)[0]}_{suffix}{os.path.splitext(filename)[1]}"
                zoomed_img.save(os.path.join(output_directory, zoomed_filename))
                print(f"Saved zoomed image: {zoomed_filename}")

# Specify the input and output directories
input_directory = r"./Crop Jaundice"
output_directory = r"./Augmented Jaundice"
augment_images(input_directory, output_directory)