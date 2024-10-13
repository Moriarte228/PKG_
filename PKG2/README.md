**Image Information Extractor**

This Python script enables you to select a folder containing images and extract details such as the image name, size, resolution, color depth, and compression type. It also includes an option to save the extracted data to a CSV file and displays the information in a graphical user interface (GUI) using Tkinter.

**Prerequisites**
- Python 3.x
- Required Python libraries: 
  - `os`
  - `pandas`
  - `tkinter` (part of the Python standard library)
  - `PIL` (Python Imaging Library, commonly referred to as Pillow)

**Usage**
1. Run the script.
2. Click the "Select Image Folder" button to choose a folder containing images.
3. The script will recursively search the selected folder and its subdirectories for image files (with extensions such as .jpg, .jpeg, .png, .gif, .bmp).
4. Information about the images will be displayed in a table within a new Tkinter window.
5. You can save the displayed data as a CSV file by clicking the "Save as CSV" button. The script will prompt you to choose a location and filename for the CSV file.

**Customization**
Feel free to modify the script to fit your needs. You can adjust the supported image file extensions, tweak the appearance of the Tkinter table, or change other aspects of the script as necessary.

**Contributing**
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
