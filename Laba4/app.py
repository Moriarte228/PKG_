import tkinter as tk
from tkinter import ttk
import time
import ttkbootstrap as tb
from matplotlib.colors import to_rgb

# Настройки окна
WIDTH, HEIGHT = 1000, 1000  # Увеличенный размер окна
BACKGROUND_COLOR = "white"
GRID_COLOR = "lightgray"
AXIS_COLOR = "black"
CELL_COLOR = "red"
CELL_INTENSITY = 1.0

# Масштаб системы координат
scale = 40

# Инициализация окна с использованием темы ttkbootstrap
root = tb.Window(themename="cosmo")
root.title("Демонстрация алгоритмов растеризации")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack(pady=10)


# Функция для рисования сетки и системы координат
def draw_grid():
    canvas.delete("all")
    mid_x, mid_y = WIDTH // 2, HEIGHT // 2

    # Рисуем вертикальные линии сетки
    for x in range(mid_x % scale, WIDTH, scale):
        canvas.create_line(x, 0, x, HEIGHT, fill=GRID_COLOR)

    # Рисуем горизонтальные линии сетки
    for y in range(mid_y % scale, HEIGHT, scale):
        canvas.create_line(0, y, WIDTH, y, fill=GRID_COLOR)

    # Рисуем оси
    canvas.create_line(mid_x, 0, mid_x, HEIGHT, fill=AXIS_COLOR, width=2)  # Вертикальная ось
    canvas.create_line(0, mid_y, WIDTH, mid_y, fill=AXIS_COLOR, width=2)  # Горизонтальная ось

    # Подписи для осей
    for x in range(mid_x % scale, WIDTH, scale):
        coord_x = (x - mid_x) // scale
        if coord_x != 0:
            canvas.create_text(x, mid_y + 10, text=str(coord_x), fill=AXIS_COLOR, font=("Arial", 8))
    for y in range(mid_y % scale, HEIGHT, scale):
        coord_y = (mid_y - y) // scale
        if coord_y != 0:
            canvas.create_text(mid_x + 10, y, text=str(coord_y), fill=AXIS_COLOR, font=("Arial", 8))


# Функция для закрашивания ячейки сетки
def fill_cell(x, y, color=CELL_COLOR, intensity=CELL_INTENSITY):
    mid_x, mid_y = WIDTH // 2, HEIGHT // 2
    x1 = mid_x + x * scale
    y1 = mid_y - y * scale
    x2 = x1 + scale
    y2 = y1 - scale
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


# Алгоритмы растеризации
def step_by_step(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):  # Основная ось - X
        if x1 > x2:  # Убедимся, что идем слева направо
            x1, y1, x2, y2 = x2, y2, x1, y1
        k = dy / dx if dx != 0 else 0
        y = y1
        for x in range(x1, x2 + 1):
            fill_cell(x, round(y), "red")
            y += k
    else:  # Основная ось - Y
        if y1 > y2:  # Убедимся, что идем снизу вверх
            x1, y1, x2, y2 = x2, y2, x1, y1
        if dy != 0:
            k = dx / dy
        else:
             k = 0
        x = x1
        for y in range(y1, y2 + 1):
            fill_cell(round(x), y, "red")
            x += k




def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0
    for _ in range(steps + 1):
        fill_cell(round(x), round(y), color="blue")
        x += x_inc
        y += y_inc


def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        fill_cell(x0, y0, color="green")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy




def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    while x <= y:
        fill_cell(xc + x, yc + y, color="purple")
        fill_cell(xc - x, yc + y, color="purple")
        fill_cell(xc + x, yc - y, color="purple")
        fill_cell(xc - x, yc - y, color="purple")
        fill_cell(xc + y, yc + x, color="purple")
        fill_cell(xc - y, yc + x, color="purple")
        fill_cell(xc + y, yc - x, color="purple")
        fill_cell(xc - y, yc - x, color="purple")
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1


# Функция для выполнения выбранного алгоритма
def execute_algorithm(algorithm):
    try:
        x0 = int(x0_entry.get())
        y0 = int(y0_entry.get())
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        start_time = time.time()
        draw_grid()
        if algorithm == "step_by_step":
            step_by_step(x0, y0, x1, y1)
        elif algorithm == "dda":
            dda(x0, y0, x1, y1)
        elif algorithm == "bresenham_line":
            bresenham_line(x0, y0, x1, y1)
        elif algorithm == "bresenham_circle":
            r = int(r_entry.get())
            bresenham_circle(x0, y0, r)
        end_time = time.time()
        time_label.config(text=f"Время работы: {end_time - start_time:.6f} секунд")
    except ValueError:
        time_label.config(text="Ошибка: введите корректные данные!")


# Функция для обновления масштаба
def update_scale():
    global scale
    try:
        scale = int(scale_entry.get())
        draw_grid()
    except ValueError:
        time_label.config(text="Ошибка: введите корректное значение масштаба!")


# Интерфейс
frame = ttk.Frame(root, padding=10)
frame.pack()

# Поля ввода и подписи
ttk.Label(frame, text="Начальная точка (x0, y0):").grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
x0_entry = ttk.Entry(frame, width=10)
y0_entry = ttk.Entry(frame, width=10)
x0_entry.grid(row=1, column=0)
y0_entry.grid(row=1, column=1)

ttk.Label(frame, text="Конечная точка (x1, y1):").grid(row=2, column=0, columnspan=2, pady=5, sticky="w")
x1_entry = ttk.Entry(frame, width=10)
y1_entry = ttk.Entry(frame, width=10)
x1_entry.grid(row=3, column=0)
y1_entry.grid(row=3, column=1)

ttk.Label(frame, text="Радиус (для окружности):").grid(row=4, column=0, pady=5, sticky="w")
r_entry = ttk.Entry(frame, width=10)
r_entry.grid(row=4, column=1)

ttk.Label(frame, text="Масштаб (размер клетки):").grid(row=5, column=0, pady=5, sticky="w")
scale_entry = ttk.Entry(frame, width=10)
scale_entry.insert(0, "40")
scale_entry.grid(row=5, column=1)

# Кнопки
ttk.Button(frame, text="Обновить масштаб", command=update_scale).grid(row=6, column=0, columnspan=2, pady=10)
ttk.Button(frame, text="Пошаговый алгоритм", command=lambda: execute_algorithm("step_by_step")).grid(row=7, column=0,
                                                                                                     columnspan=2,
                                                                                                     pady=5)
ttk.Button(frame, text="Алгоритм ЦДА", command=lambda: execute_algorithm("dda")).grid(row=8, column=0, columnspan=2,
                                                                                      pady=5)
ttk.Button(frame, text="Алгоритм Брезенхема (прямая)", command=lambda: execute_algorithm("bresenham_line")).grid(row=9,
                                                                                                                 column=0,
                                                                                                                 columnspan=2,
                                                                                                                 pady=5)
ttk.Button(frame, text="Алгоритм Брезенхема (окружность)", command=lambda: execute_algorithm("bresenham_circle")).grid(
    row=10, column=0, columnspan=2, pady=5)


# Вывод времени
time_label = ttk.Label(root, text="Время работы: ")
time_label.pack(pady=10)

# Инициализация
draw_grid()
root.mainloop()
