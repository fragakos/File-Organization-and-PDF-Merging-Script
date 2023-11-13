import sys, os
from PIL import Image

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python fileOrganization.py <folder_path>")
else:
    # Get folder path from command-line argument
    folder_path = sys.argv[1]
    prefixes = ["./00", "./01", "./02"]

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
    images = sorted([f for f in os.listdir(folder_path)], key=lambda f: f)
    try:
        for image in images:
            if image[:2] == "00":
                os.rename(f"{folder_path}{image}", f"./00/{image}")
            elif image[:2] == "01":
                os.rename(f"{folder_path}{image}", f"./01/{image}")
            else:
                os.rename(f"{folder_path}{image}", f"./02/{image}")
    except FileNotFoundError as e:
        print(f"Error: {e} - File not found.")
    except PermissionError as e:
        print(f"Error: {e} - Permission error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        # Convert each subfolder into a PDF file
        foldersToTraverse = next(os.walk("."))[1][:3]
        for folder in foldersToTraverse:
            pdf_path = f"./{folder}.pdf"
            files = os.listdir(folder)
            if not files:
                print(f"Skipped! Warning: Folder {folder} has no images. ")
                continue
            images = []

            # Iterate over files in the folder
            for f in files:
                try:
                    # Attempt to open the image file
                    image_path = f"./{folder}/" + f
                    image = Image.open(image_path)
                    images.append(image)
                except Exception as e:
                    print(f"Error opening image {image_path}: {e}")

                # Check if there are no valid images in the folder
                if not images:
                    print(
                        f"Warning: No valid images found in folder {folder}. Skipping."
                    )
                    continue
            # Save images in the subfolder as a PDF file
            images[0].save(
                pdf_path,
                "PDF",
                resolution=100.0,
                save_all=True,
                append_images=images[1:],
            )
    except Exception as e:
        print(f"Error: {e}")
