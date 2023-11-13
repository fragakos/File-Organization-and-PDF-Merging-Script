from PIL import Image, ImageDraw
import random, os, sys

def createTempImages(n, path):
    # Check if the specified path exists
    if not os.path.exists(path):
        # If it does not exist, create the directory
        os.makedirs(path)
    else:
        file_list = os.listdir(path)
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            os.remove(file_path)    
    # List of colors to be used for image creation
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    # List of prefixes to be used for image names
    prefixes  = ["00", "01", "02"]
    # Generate and save n images
    for i in range(n):
        # Create a new image with a random background color
        img = Image.new('RGB', (300, 200), color=random.choice(colors))
        # Get a drawing context on the image
        draw = ImageDraw.Draw(img)
        # Draw a rectangle with a random fill color
        draw.rectangle([50, 50, 250, 150], fill=random.choice(colors))
        # Save the image to the specified "path" location
        # Image will have a name starting with '00', '01', or '02' randomly,
        # followed by 5 random numbers.
        # If there are still prefixes to use, choose one from the list
        if prefixes:
            prefix = prefixes.pop(0)
        else:
            # If all prefixes have been used, choose randomly
            prefix = random.choice(["00", "01", "02"])
        rest = ''.join(str(random.randint(0, 9)) for _ in range(5))
        img.save(f"{path}/{prefix}{rest}.png")


if len(sys.argv) != 2:
        print("Usage: python createFiles.py <folder_name>")
else:
    # Get folder path from command-line argument
    folder_name = sys.argv[1]
    
    createTempImages(10, f"{folder_name}")

