import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt


#Example.txt for lianga-barskiy
#OtherExample.txt for sutherland_hodgman

def select_file():
    """
    Открывает диалог для выбора файла.
    """
    file_path = filedialog.askopenfilename(title="Выберите файл с входными данными",
                                           filetypes=[("Text Files", "*.txt")])
    if file_path:
        global segments, clip_window
        segments, clip_window = read_input(file_path)
        if segments and clip_window:
            messagebox.showinfo("Успех", "Файл успешно загружен.")
        else:
            segments, clip_window = None, None

def read_input(file_path):
    """
    Считывает данные из файла и возвращает список отрезков и координаты окна отсечения.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            n = int(lines[0].strip())
            segments = [list(map(float, lines[i].strip().split())) for i in range(1, n + 1)]
            clip_window = list(map(float, lines[n + 1].strip().split()))
            return segments, clip_window
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось считать файл: {e}")
        return None, None
def read_data_from_file():
    """Чтение данных из файла с помощью диалогового окна."""
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    file_path = filedialog.askopenfilename(title="Выберите файл с координатами", filetypes=[("Text Files", "*.txt")])

    with open(file_path, "r") as file:
        data = file.readlines()

    # Считываем координаты вершин многоугольника
    n = int(data[0].strip())  # Количество вершин
    polygon = []
    for i in range(1, n + 1):
        x, y = map(float, data[i].split())
        polygon.append((x, y))

    # Считываем координаты отсекателя
    xmin, ymin, xmax, ymax = map(float, data[n + 1].split())
    clipper = (xmin, ymin, xmax, ymax)

    return polygon, clipper

def sutherland_hodgman_clip(polygon, clipper):
    """Алгоритм Сазерленда-Ходжмана для отсечения выпуклого многоугольника."""
    xmin, ymin, xmax, ymax = clipper

    def inside(point, edge):
        """Проверяет, находится ли точка внутри отсекателя."""
        x, y = point
        if edge == "LEFT":
            return x >= xmin
        elif edge == "RIGHT":
            return x <= xmax
        elif edge == "BOTTOM":
            return y >= ymin
        elif edge == "TOP":
            return y <= ymax

    def intersect(p1, p2, edge):
        """Находит точку пересечения ребра с границей отсекателя."""
        x1, y1 = p1
        x2, y2 = p2

        if edge == "LEFT":
            x, y = xmin, y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
        elif edge == "RIGHT":
            x, y = xmax, y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
        elif edge == "BOTTOM":
            x, y = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin
        elif edge == "TOP":
            x, y = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax

        return x, y

    def clip_edge(polygon, edge):
        """Отсекает многоугольник относительно одной границы."""
        clipped_polygon = []
        for i in range(len(polygon)):
            curr_point = polygon[i]
            prev_point = polygon[i - 1]

            if inside(curr_point, edge):
                if not inside(prev_point, edge):
                    # Точка входит в отсекатель — добавляем пересечение
                    clipped_polygon.append(intersect(prev_point, curr_point, edge))
                # Добавляем текущую точку
                clipped_polygon.append(curr_point)
            elif inside(prev_point, edge):
                # Точка выходит из отсекателя — добавляем пересечение
                clipped_polygon.append(intersect(prev_point, curr_point, edge))

        return clipped_polygon

    # Отсечение по всем границам отсекателя
    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]
    for edge in edges:
        polygon = clip_edge(polygon, edge)

    return polygon


def liang_barsky(clip_window, segment):
    """
    Реализует алгоритм Лианга-Барски для отсечения одного отрезка.
    """
    x1, y1, x2, y2 = segment
    xmin, ymin, xmax, ymax = clip_window

    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Отрезок вне окна
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)
        if u1 > u2:
            return None  # Отрезок невидим

    x1_clipped = x1 + u1 * dx
    y1_clipped = y1 + u1 * dy
    x2_clipped = x1 + u2 * dx
    y2_clipped = y1 + u2 * dy

    return [x1_clipped, y1_clipped, x2_clipped, y2_clipped]


def plot_segments(segments, clipped_segments, clip_window):
    """
    Создает график с исходными и отсеченными отрезками.
    """
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)

    # Рисуем окно отсечения
    xmin, ymin, xmax, ymax = clip_window
    rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                     edgecolor='red', fill=False, linewidth=2, label='Окно отсечения')
    ax.add_patch(rect)

    # Рисуем исходные отрезки
    for seg in segments:
        x1, y1, x2, y2 = seg
        ax.plot([x1, x2], [y1, y2], 'b--', label='Исходные отрезки' if 'Исходные отрезки' not in ax.get_legend_handles_labels()[1] else None)

    # Рисуем отсеченные отрезки
    for seg in clipped_segments:
        if seg:
            x1, y1, x2, y2 = seg
            ax.plot([x1, x2], [y1, y2], 'g-', linewidth=2, label='Отсеченные отрезки' if 'Отсеченные отрезки' not in ax.get_legend_handles_labels()[1] else None)

    ax.legend()
    ax.grid(True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Отсечение отрезков алгоритмом Лианга-Барски')

    return fig

def plot_polygon(polygon, clipper, clipped_polygon):
    """Визуализация исходного и отсечённого многоугольника."""
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    xmin, ymin, xmax, ymax = clipper
    rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                     edgecolor='red', fill=False, linewidth=2, label='Окно отсечения')
    ax.add_patch(rect)

    # Рисуем отсекатель
    ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'g-', label="Отсекатель")

    # Рисуем исходный многоугольник
    if polygon:
        poly_x, poly_y = zip(*(polygon + [polygon[0]]))  # Замыкаем многоугольник
        ax.plot(poly_x, poly_y, 'b--', label="Исходный многоугольник")

    # Рисуем отсечённый многоугольник
    if clipped_polygon:
        clipped_x, clipped_y = zip(*(clipped_polygon + [clipped_polygon[0]]))  # Замыкаем отсечённый многоугольник
        ax.plot(clipped_x, clipped_y, 'r-', label="Отсечённый многоугольник")

    ax.legend()
    ax.grid(True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Отсечение выпуклого многоугольника алгоритмом')

    return fig


def process_clipping():
    select_file()
    if not segments or not clip_window:
        messagebox.showwarning("Внимание", "Сначала выберите файл с данными!")
        return

    clipped_segments = [liang_barsky(clip_window, seg) for seg in segments]
    fig = plot_segments(segments, clipped_segments, clip_window)

    # Встраиваем график в интерфейс
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    canvas.draw()

def process_clipping2():
    polygon, clipper = read_data_from_file()

    clipped_polygon = sutherland_hodgman_clip(polygon, clipper)

    # Встраиваем график в интерфейс
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(plot_polygon(polygon, clipper, clipped_polygon), master=canvas_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    canvas.draw()


# Создание интерфейса
root = tk.Tk()
root.title("Отсечение отрезков")

# Глобальные переменные для хранения данных
segments = None
clip_window = None

# Основной фрейм для графика
canvas_frame = tk.Frame(root, width=600, height=600, bg="white")
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Панель кнопок
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=10)


btn_process = tk.Button(button_frame, text="Отсечь отрезки", command=process_clipping)
btn_process.pack(side=tk.LEFT, padx=5)

btn_process1 = tk.Button(button_frame, text="Отсечь выпуклый многоугольник",
                         command=process_clipping2)
btn_process1.pack(side=tk.LEFT, padx=5)

# Запуск приложения
root.mainloop()
