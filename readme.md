These are two Python scripts and a text file for instructions.
The scripts are named createFiles.py and fileOrganization.py, and the text file is named requirements.txt.

# Here's a brief explanation of how to use the scripts:

createFiles.py: This script generates and saves a specified number of images with random background colors and rectangles. To use this script, follow these steps:

Run the script in your terminal or command prompt with the folder name as an argument: python createFiles.py <folder_name>

The script will create 10 images in the specified folder with random background colors and rectangles.

===========================================================================================================================================================================

fileOrganization.py: This script sorts and organizes images in a specified folder into subfolders based on their filename prefixes. To use this script, follow these steps:

Run the script in your terminal or command prompt with the folder path as an argument: python fileOrganization.py <folder_path>

The script will create or clear existing directories with the specified prefixes, sort images in the folder, and convert each subfolder into a PDF file.

===========================================================================================================================================================================

requirements.txt: This file contains the required Python libraries for the scripts. To install the libraries, run the following command:
pip install -r requirements.txt

===========================================================================================================================================================================

Example Execute:

1. pip install -r requirements.txt

2. python createFiles.py startingFiles

3. python fileOrganization.py .\startingFiles\
