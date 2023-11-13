import sys, os
from PIL import Image

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
        print("Usage: python fileOrganization.py <folder_path>")
else:
    # Get folder path from command-line argument
    folder_path = sys.argv[1]
    prefixes  = ["./00", "./01", "./02"]

    # Create or clear existing directories with specified prefixes
    for prefix in prefixes:
        if not os.path.exists(prefix):
            # If it does not exist, create the directory
            os.makedirs(prefix)  
        else:
            # If it exists, remove all files in the directory
            file_list = os.listdir(prefix)
            for file_name in file_list:
                file_path = os.path.join(prefix, file_name)
                os.remove(file_path)

    # Sort images in the specified folder and organize them into subfolders based on filename prefixes
    images = sorted([f for f in os.listdir(folder_path)], key = lambda f : f)
    for image in images:
         if(image[:2] == "00"):
              os.rename(f"{folder_path}{image}", f"./00/{image}")
         elif(image[:2] == "01"):
              os.rename(f"{folder_path}{image}", f"./01/{image}")
         else:
              os.rename(f"{folder_path}{image}", f"./02/{image}")

    # Convert each subfolder into a PDF file
    foldersToTraverse = next(os.walk('.'))[1][:3]
    for folder in foldersToTraverse:
         pdf_path = f"./{folder}.pdf"
         files = os.listdir(folder)
         images = [Image.open(f"./{folder}/" + f) for f in os.listdir(f"./{folder}")]
         # Save images in the subfolder as a PDF file
         images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

            