import os
import sys
import shutil


file_types = {
    "Images": [".jpg", ".png"],
    "Music": [".flac", ".mp3", ".wav"],
    "Documents": [".txt", ".md", ".pdf", ".docx", ".xlsx", ".pptx"],
    "Archives": [".gz", ".zip", ".rar", ".tar"],
    "Videos": [".mp4", ".mkv", ".avi"]
    }


def sort_directory(directory_string, file_types):

    for filename in os.listdir(directory_string):
        file_path = os.path.join(directory_string, filename)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        moved = False
        
        for category, extensions in file_types.items():
            if extension in extensions:


                dest_folder = os.path.join(directory_string, category)

                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break
        
        if not moved:
            others_folder = os.path.join(directory_string, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

    print("Success!")

        





if __name__ == "__main__":
    current_directory = os.getcwd()

    print(current_directory)

    confirm = input("is this the directory you want to sort? (y/n)").strip().lower()

    if confirm == "y":
        sort_directory(current_directory, file_types)
    elif confirm == "n":
        current_directory = input("Enter your desired directory (CAREFUL!): ").strip()
        sort_directory(current_directory, file_types)
    else:
        print("You didn't enter a valid input. Exiting..")
        sys.exit()
