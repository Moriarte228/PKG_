# Clipping Algorithms Visualization Tool

This Python application provides a graphical interface for visualizing clipping algorithms, specifically the **Liang-Barsky** algorithm for line clipping and the **Sutherland-Hodgman** algorithm for convex polygon clipping. The tool allows users to load input data from a file, process clipping, and view the results on an interactive plot.

## Features

- **Liang-Barsky Algorithm**: Clips line segments against a rectangular clipping window.
- **Sutherland-Hodgman Algorithm**: Clips a convex polygon against a rectangular clipping window.
- **File Input**: Easily load input data from `.txt` files.
- **Visualization**: View the original and clipped geometry with matplotlib plots embedded in a Tkinter interface.

## Requirements

- Python 3.7+
- Required Python libraries:
  - `tkinter`
  - `matplotlib`

Install the required libraries with:
```bash
pip install matplotlib tkinter
```

## How to Use

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Load Data**:
   - Click **"Отсечь отрезки"** to load a file for line clipping.
   - Click **"Отсечь выпуклый многоугольник"** to load a file for polygon clipping.

3. **File Format**:
   - For the Liang-Barsky algorithm:
     - The first line contains the number of line segments, `N`.
     - The next `N` lines specify the endpoints of each line segment as `x1 y1 x2 y2`.
     - The last line contains the coordinates of the clipping window as `xmin ymin xmax ymax`.
   - For the Sutherland-Hodgman algorithm:
     - The first line contains the number of vertices in the polygon, `N`.
     - The next `N` lines specify the polygon's vertices as `x y`.
     - The final line contains the coordinates of the clipping window as `xmin ymin xmax ymax`.

4. **Process Clipping**:
   - Click the respective button to visualize the results. The application will display the original and clipped geometry.

5. **Graphical Interface**:
   - The plot shows the clipping window, original geometry, and clipped geometry with distinct styles.

## Example Input Files

### Liang-Barsky Example (Example.txt)
```
2
0 0 5 5
-2 3 6 7
1 1 4 4
```

### Sutherland-Hodgman Example (OtherExample.txt)
```
4
1 1
4 1
4 4
1 4
2 2 3 3
```


## Code Structure

- **`select_file()`**: Opens a file dialog to select input files for line clipping.
- **`read_input()`**: Parses line clipping input files.
- **`read_data_from_file()`**: Parses polygon clipping input files.
- **`sutherland_hodgman_clip()`**: Implements the Sutherland-Hodgman algorithm.
- **`liang_barsky()`**: Implements the Liang-Barsky algorithm.
- **`plot_segments()`**: Visualizes line clipping results.
- **`plot_polygon()`**: Visualizes polygon clipping results.
- **`process_clipping()`**: Handles the line clipping workflow.
- **`process_clipping2()`**: Handles the polygon clipping workflow.

## Customization

You can modify the visualization styles or add support for additional clipping algorithms by editing the provided functions.

