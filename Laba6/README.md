# 3D Object Manipulation and Visualization Tool

This Python application provides an interactive environment for 3D object visualization and manipulation. Using OpenGL and PyGame, the program renders a 3D object and allows users to rotate, translate, scale, and view 2D projections of the object.

## Features

- **Interactive Manipulation**:
  - Rotate the object using the mouse.
  - Translate the object using arrow keys.
  - Scale the object using `W` (zoom in) and `S` (zoom out).
- **2D Projections**:
  - View projections of the object onto:
    - `XY` plane (`Z` key)
    - `XZ` plane (`Y` key)
    - `YZ` plane (`X` key)
- **Visualized Axes**:
  - Red: X-axis
  - Green: Y-axis
  - Blue: Z-axis

## Requirements

- Python 3.7+
- Required Python libraries:
  - `pygame`
  - `PyOpenGL`
  - `numpy`
  - `matplotlib`

Install the required libraries with:
```bash
pip install pygame PyOpenGL numpy matplotlib
```

## How to Run

1. Save the script as `main.py`.
2. Run the script:
   ```bash
   python main.py
   ```

## Controls

| Action                     | Control           |
|----------------------------|-------------------|
| Rotate object              | Drag with Left Mouse Button |
| Translate object           | Arrow keys        |
| Scale object               | `W` (zoom in), `S` (zoom out) |
| View XY projection         | Press `Z`         |
| View XZ projection         | Press `Y`         |
| View YZ projection         | Press `X`         |
| Exit program               | Close the window  |

## Code Overview

### Vertices and Edges
- **Vertices**: Defines the 3D coordinates of the object's points.
- **Edges**: Defines connections between vertices to form the object's shape.

### Axes Drawing
- Visualizes X, Y, and Z axes with different colors to guide the orientation of the object.

### Transformations
- **Rotation**: A custom rotation matrix is created to rotate the object based on mouse input.
- **Translation**: Adjusts the object's position using arrow key inputs.
- **Scaling**: Uniformly scales the object
- **Transformation matrix**: You can see transformation matrix in console

### Projections
- Generates 2D projections of the object on `XY`, `XZ`, and `YZ` planes using matplotlib.

## Example Transformation Matrix

The transformation matrix combines scaling, rotation, and translation:
```plaintext
[[sx*r11, sx*r12, sx*r13, tx],
 [sy*r21, sy*r22, sy*r23, ty],
 [sz*r31, sz*r32, sz*r33, tz],
 [  0,      0,      0,     1]]
```
Where:
- `sx`, `sy`, `sz` are scaling factors.
- `r11` to `r33` are rotation matrix components.
- `tx`, `ty`, `tz` are translation values.

