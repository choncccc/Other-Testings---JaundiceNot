import os
import shutil
import random

def split_dataset(input_directory, output_directory, train_pct=0.6, test_pct=0.2, val_pct=0.2):
    # Create output directories if they don't exist
    train_dir = os.path.join(output_directory, 'train')
    test_dir = os.path.join(output_directory, 'test')
    val_dir = os.path.join(output_directory, 'validate')
    
    for dir_path in [train_dir, test_dir, val_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    files = os.listdir(input_directory)
    
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    random.shuffle(image_files)
    
    total_images = len(image_files)
    train_count = int(total_images * train_pct)
    test_count = int(total_images * test_pct)
    val_count = total_images - train_count - test_count
    
    train_files = image_files[:train_count]
    test_files = image_files[train_count:train_count + test_count]
    val_files = image_files[train_count + test_count:]
    
    for filename in train_files:
        shutil.move(os.path.join(input_directory, filename), os.path.join(train_dir, filename))
    
    for filename in test_files:
        shutil.move(os.path.join(input_directory, filename), os.path.join(test_dir, filename))
    
    for filename in val_files:
        shutil.move(os.path.join(input_directory, filename), os.path.join(val_dir, filename))
    
    print(f"Moved {train_count} files to {train_dir}")
    print(f"Moved {test_count} files to {test_dir}")
    print(f"Moved {val_count} files to {val_dir}")

# Specify the input and output directories
input_directory = r"./Crop Jaundice"
output_directory = r"./new/Jaundced Class1"
split_dataset(input_directory, output_directory)