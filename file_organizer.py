# Python File Organizer Version 1.0.0

import os
import shutil

FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Audio': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.rar'],
    'Others': []
}

def organize_directory(directory_path):
    for filename in os.listdir(directory_path):
        
        file_extension = os.path.splitext(filename)[1].lower()
        
        # File extensiion = the "butt" of each file (e.g. .csv)
        # .splittext() = split betwwen the dots (e.g. "nodeptrai.jpg" will become "nodeptrai" & ".jpg")

        if os.path.isdir(os.path.join(directory_path, filename)) or filename.startswith('.'):
            continue
        
        # Skipping hidden files
        # os.path.isdir() checks if one is a directory or not
        # .startswith('.') check if one is a blank file or not such as .git or .DS_Store
        

        destination_folder = None
        
        # Setting the destination to none every loop
        
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = category
                break
        
        # If the extension exists in the category, the variable destination_folder will be assigned with the corresponding category
        # category = category in FILE_CATEGORIES
        # extensions = all the file extensions in the categories of FILE_CATEGORIES
        
        if destination_folder is None:
            destination_folder = 'Others'
        
        # If the extension doesn't exist then add it to the 'Others' category (which is unlikely to happen)

        destination_path = os.path.join(directory_path, destination_folder)
        
        # Join the directory path with the corresponding destination
        
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        
        # Check if the directory path exists or not; if not, create a new one

        source_file = os.path.join(directory_path, filename)
        destination_file = os.path.join(destination_path, filename)
        shutil.move(source_file, destination_file)
        
        # Moving from the original source file to the appropriate destination
        # source_file finds the originial source
        # destination_file determines the newly-redirected source
        
        print(f"Moved: {filename} to {destination_folder}/")
        
        # Print to the terminal

if __name__ == "__main__":
    folder_to_organize = input("Enter the path to the folder you want to organize: ")
    
    # Let the user determine what file they want to reorganize
    
    if os.path.isdir(folder_to_organize):
        organize_directory(folder_to_organize)
        print("Organization complete!")
    else:
        print(f"The path '{folder_to_organize}' is not valid.")
        
    # Announcing the process
