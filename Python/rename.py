import os

# Set the pathto your folder
image_folder = "C:\\Users\\Julian\\Desktop\\python"

# Get a list of all files in the folder
file_list = os.listdir(image_folder)

# Sort the list to ensure sequential ordering
file_list.sort()

# Specify a base name for your renamed images
new_name_base = 'pythons'

# Counter to keep track of the sequential number
count = 1

# Loop through the files and rename them sequentially
for old_name in file_list:
    # Get the file extension 
    file_extension = os.path.splitext(old_name)[1]
    
    # Create the new name
    new_name = f"{name_name_base}_{count03d}{file_extension}"

    # Construct the full paths
    old_path = os.path.join(image_folder, old_name)
    new_path = os.path.join(image folder, new_name)

    #Rename the file 
    os.rename(old path,new_path)

    # Increment the counter 
    count += 1

print("Renaming completed")