# Image Processing Application

## Overview

The **Image Processing Application** is a desktop tool for applying various image processing techniques using Python libraries such as OpenCV, NumPy, and Tkinter. The application provides a graphical user interface (GUI) for users to load images, apply filters, enhance contrast, and perform histogram equalization.

---

## Features

### 1. **Load Image**
   - Allows users to select an image file from their system.
   - The image is resized to fit the application window (600x450 pixels) for display purposes.

### 2. **Display Original Image**
   - Displays the original image in its own frame.

### 3. **Display Processed Image**
   - Shows the output of the selected processing technique in a separate frame.

### 4. **Image Processing Techniques**
   - **Median Filter:**
     - Removes noise while preserving edges by applying a median blur.
   - **Linear Contrast Adjustment:**
     - Stretches the intensity range of the image to enhance contrast.
   - **Histogram Equalization (RGB):**
     - Equalizes each color channel (R, G, B) to improve color distribution.
   - **Histogram Equalization (HSV):**
     - Equalizes the histogram of the value (brightness) channel in the HSV color space.

---

## Installation

1. **Prerequisites**
   - Python 3.x installed on your system.
   - Required libraries:
     ```bash
     pip install opencv-python numpy pillow
     ```

2. **Run the Application**
   - Save the code into a file, e.g., `app.py`.
   - Run the script using:
     ```bash
     python app.py
     ```

---

## GUI Components

### **Main Window**
   - **Title:** *Image Processing Application*
   - **Size:** 1800x900 pixels
   - **Background:** Light grey (`#f0f0f0`)

### **Frames**
   - **Original Image Frame:** Left side for the static/original image.
   - **Processed Image Frame:** Right side for displaying processed results.

### **Buttons**
   - **Load Image:** Opens a file dialog to select an image.
   - **Apply Median Filter:** Applies a median filter to reduce noise.
   - **Apply Linear Contrast:** Adjusts image contrast using linear stretching.
   - **Equalize Histogram (RGB):** Applies histogram equalization on the RGB channels.
   - **Equalize Histogram (HSV):** Applies histogram equalization on the HSV color space.

---

## Code Structure

### **Classes**
- **`ImageProcessor`**
  - Handles the GUI setup and image processing operations.
  
### **Methods**
- **`load_images`:** Loads and displays the original image.
- **`show_static_image`:** Displays the original image in the static image frame.
- **`show_processed_image`:** Displays processed images in the processed image frame.
- **`apply_median_filter`:** Applies a median filter to the image.
- **`apply_linear_contrast`:** Enhances contrast through linear stretching.
- **`equalize_histogram_rgb`:** Equalizes histograms for each RGB channel.
- **`histogram_equalization_hsv`:** Equalizes the histogram of the value channel in the HSV space.

---

## Usage Instructions

1. **Launch the Application:**
   - Open the application by running the script.
   
2. **Load an Image:**
   - Click the "Load Image" button to select an image.

3. **Apply Filters:**
   - Use the corresponding buttons to apply desired processing techniques.

4. **View Results:**
   - The processed image is displayed in the "Processed Image" frame.

---

## Example Workflow

1. Start the application.
2. Load an image by clicking "Load Image."
3. Click "Apply Median Filter" to reduce noise.
4. Experiment with "Apply Linear Contrast" to enhance the image's dynamic range.
5. Try "Equalize Histogram RGB" or "Equalize Histogram HSV" to adjust brightness or improve contrast.

---

## Notes

- **Supported File Formats:** JPEG, PNG, BMP, etc.
- **Image Resizing:** All images are resized to 600x450 pixels for consistent display.
- **GUI Customization:** You can modify colors, fonts, or layout as per your requirements in the code.

---

This documentation provides a comprehensive guide to understanding, using, and modifying the Image Processing Application. Enjoy exploring your images!
