import pandas as pd
import os
import shutil

# Specify the path to your CSV file
csv_file_path = r'.\valid\_annotations.csv' # Update with your CSV file path
# Specify the base directory where the images are stored
images_base_dir = r'.\valid'  # Update with the directory containing your images
# Specify the target directory where you want to organize the images
target_base_dir = r'.\preprocessed_data'  # Update with your target directory

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Create target base directory if it doesn't exist
if not os.path.exists(target_base_dir):
    os.makedirs(target_base_dir)

# Iterate through the DataFrame and organize images
for index, row in df.iterrows():
    # Get the filename and class from the row
    filename = row['filename']
    class_label = row['class']
    
    # Create a target directory for the class if it doesn't exist
    class_dir = os.path.join(target_base_dir, class_label)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)
    
    # Construct full file paths
    src_path = os.path.join(images_base_dir, filename)
    dst_path = os.path.join(class_dir, filename)
    
    # Move the image to the respective class directory
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
    else:
        print(f"Warning: {src_path} does not exist.")

print("Images have been organized successfully.")
