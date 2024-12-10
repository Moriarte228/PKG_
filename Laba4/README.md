# Rasterization Algorithm Visualization

## Overview

The **Rasterization Algorithm Visualization** application is a GUI tool built with `tkinter` and `ttkbootstrap` that demonstrates various rasterization algorithms. It allows users to visualize grid-based rasterization techniques, such as step-by-step line drawing, the DDA algorithm, Bresenham's line algorithm, and Bresenham's circle algorithm.

---

## Features

### Visualization
- Interactive grid-based visualization of rasterization algorithms.
- Customizable grid scaling for fine-tuning visualization.
- Supports rendering lines and circles on a Cartesian coordinate grid.

### Algorithms Supported
1. **Step-by-Step Line Drawing**
2. **Digital Differential Analyzer (DDA)**
3. **Bresenham's Line Algorithm**
4. **Bresenham's Circle Algorithm**

### User Interface
- Input fields for start and end coordinates.
- Real-time updates of the coordinate grid based on user-defined scale.
- Execution time display for each algorithm.

---

## Installation

1. **Prerequisites**
   - Python 3.x installed on your system.
   - Required libraries:
     ```bash
     pip install ttkbootstrap
     ```

2. **Run the Application**
   - Save the code into a file, e.g., `app.py`.
   - Run the script using:
     ```bash
     python app.py
     ```

---

## Usage Instructions

1. **Launch the Application**
   - Run the script in your Python environment to open the application window.

2. **Input Coordinates**
   - Enter start `(x0, y0)` and end `(x1, y1)` coordinates in the provided fields.
   - Optionally, enter a radius for circle rasterization.

3. **Select an Algorithm**
   - Click the corresponding button to visualize the algorithm:
     - "Step-by-Step Algorithm"
     - "DDA Algorithm"
     - "Bresenham's Line Algorithm"
     - "Bresenham's Circle Algorithm"

4. **Update Grid Scale**
   - Enter a new grid cell size in the **Scale** field and click "Update Scale" to refresh the grid.

5. **View Results**
   - The grid will display the rasterized line or circle. Execution time is shown at the bottom.

---

## GUI Components

### **Main Window**
   - **Title:** *Rasterization Algorithm Visualization*
   - **Size:** 1000x1000 pixels
   - **Background:** White

### **Grid**
   - Dynamic Cartesian grid with labeled axes.
   - Adjustable cell size via the "Scale" field.

### **Controls**
   - Input fields for coordinates `(x0, y0)` and `(x1, y1)`.
   - Input field for circle radius.
   - Buttons for selecting and executing algorithms.
   - Button for refreshing grid scale.

### **Output**
   - Displays execution time for the selected algorithm.

---

## Code Structure

### **Grid Management**
- **`draw_grid`**
  - Dynamically draws the Cartesian grid and axes with labeled coordinates.

### **Algorithms**
- **Step-by-Step Algorithm (`step_by_step`)**
  - Incrementally calculates pixel positions along the line.
- **DDA Algorithm (`dda`)**
  - Uses floating-point arithmetic to interpolate pixel positions.
- **Bresenham's Line Algorithm (`bresenham_line`)**
  - Efficiently determines pixel positions using integer arithmetic.
- **Bresenham's Circle Algorithm (`bresenham_circle`)**
  - Renders circles using symmetry and efficient calculations.

### **User Interaction**
- **`execute_algorithm`**
  - Executes the selected algorithm based on user input.
- **`update_scale`**
  - Updates grid scaling and redraws the grid.

---

## Example Workflow

1. Start the application.
2. Input start `(x0, y0)` and end `(x1, y1)` coordinates.
3. Select the desired rasterization algorithm.
4. Adjust the scale if needed and visualize the result.
5. Observe the execution time displayed at the bottom.

---

## Notes

- **Default Grid Scale:** Each cell represents 1 unit in the Cartesian coordinate system, adjustable via the scale input.
- **Error Handling:** Displays error messages for invalid inputs.
- **Color Scheme:**
  - Step-by-Step: Red
  - DDA: Blue
  - Bresenham's Line: Green
  - Bresenham's Circle: Purple

This documentation provides a comprehensive guide to using and understanding the **Rasterization Algorithm Visualization** tool. Experiment and explore the inner workings of rasterization algorithms!
