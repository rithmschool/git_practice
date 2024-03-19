import os
import random

def russian_roulette_delete(directory, file_extension, num_chambers):
    # Get list of files with specified extension
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
    
    if not files:
        print("No files with the specified extension found in the directory.")
        return
    
    print(f"Found {len(files)} files with the specified extension.")

    # Shuffle the list of files
    random.shuffle(files)
    
    # Determine which chamber has the bullet
    bullet_chamber = random.randint(1, num_chambers)
    
    # Play Russian roulette
    for i, file in enumerate(files):
        print(f"Pulling trigger for file: {file}")
        if i == bullet_chamber - 1:
            print("Bang! File deleted.")
            os.remove(os.path.join(directory, file))
            return
        else:
            print("Click. Safe for now.")

    print("The gun misfired. No files were deleted.")

# Example usage
directory = "C://"
file_extension = "*"  # Specify the file extension you want to delete
num_chambers = 6  # Number of chambers in the revolver

russian_roulette_delete(directory, file_extension, num_chambers)