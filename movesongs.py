import os
import shutil

def move_mp3_files(src_folder, dst_folder):
    try:
        # Create the destination folder if it does not exist
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
            print(f"Created destination folder: {dst_folder}")

        # Check if source folder exists
        if not os.path.exists(src_folder):
            print(f"Source folder does not exist: {src_folder}")
            return

        # Iterate over all files in the source folder
        for filename in os.listdir(src_folder):
            print(f"Checking file: {filename}")
            if filename.endswith('.mp4'):
                # Construct full file path
                src_file = os.path.join(src_folder, filename)
                dst_file = os.path.join(dst_folder, filename)
                
                print(f"Preparing to move: {src_file} -> {dst_file}")

                # Move the file
                shutil.move(src_file, dst_file)
                print(f"Moved: {src_file} -> {dst_file}")
        print("All MP3 files have been moved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source folder and the destination folder
source_folder = r'path-to-folder-with-forward-slashes-with-downloaded-songs'
destination_folder = r'path-to-destination-folder-with-forward-slashes'

# Call the function to move the files
move_mp3_files(source_folder, destination_folder)
