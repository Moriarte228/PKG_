import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Frame
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing Application")
        self.master.geometry("1800x900")
        self.master.configure(bg="#f0f0f0")

        # Заголовок
        self.label = Label(master, text="Image Processing Application", font=("Arial", 24), bg="#f0f0f0")
        self.label.pack(pady=20)

        # Фреймы для изображений
        self.static_frame = Frame(master, bg="#f0f0f0")
        self.static_frame.pack(side="left", padx=20)

        self.processed_frame = Frame(master, bg="#f0f0f0")
        self.processed_frame.pack(side="right", padx=20)

        # Метки для изображений
        self.static_image_label = Label(self.static_frame, text="Original Image", font=("Arial", 16), bg="#f0f0f0")
        self.static_image_label.pack()

        self.processed_image_label = Label(self.processed_frame, text="Processed Image", font=("Arial", 16), bg="#f0f0f0")
        self.processed_image_label.pack()

        self.static_image_display = Label(self.static_frame)
        self.static_image_display.pack(pady=10)

        self.processed_image_display = Label(self.processed_frame)
        self.processed_image_display.pack(pady=10)

        # Кнопки
        self.load_button = Button(master, text="Load Image", command=self.load_images, bg="#4CAF50", fg="white", font=("Arial", 14))
        self.load_button.pack(pady=10)

        self.median_button = Button(master, text="Apply Median Filter", command=self.apply_median_filter, bg="#2196F3", fg="white", font=("Arial", 14))
        self.median_button.pack(pady=5)

        self.contrast_button = Button(master, text="Apply Linear Contrast", command=self.apply_linear_contrast, bg="#FF9800", fg="white", font=("Arial", 14))
        self.contrast_button.pack(pady=5)

        self.equalize_button_rgb = Button(master, text="Equalize Histogram RGB", command=self.histogram_equalization_rgb, bg="#9C27B0", fg="white", font=("Arial", 14))
        self.equalize_button_rgb.pack(pady=5)

        self.equalize_button_hsv = Button(master, text="Equalize Histogram HSV",
                                          command=self.histogram_equalization_hsv, bg="#9C27B0", fg="white",
                                          font=("Arial", 14))
        self.equalize_button_hsv.pack(pady=5)

        # Переменные для изображений
        self.static_image = None
        self.original_image = None
        self.fixed_size = (600, 450)  # Фиксированный размер изображения

    def load_images(self):
        # Выбор изображения для обработки
        image_path = filedialog.askopenfilename(title="Select Image for Processing")
        if image_path:
            self.original_image = cv2.imread(image_path)
            self.original_image = cv2.resize(self.original_image, self.fixed_size)  # Изменение размера изображения
            self.show_processed_image(self.original_image)
            self.static_image = cv2.imread(image_path)
            self.static_image = cv2.resize(self.static_image, self.fixed_size)  # Изменение размера изображения
            self.show_static_image()

    def show_static_image(self):
        if self.static_image is not None:
            image = cv2.cvtColor(self.static_image, cv2.COLOR_BGR2RGB)  # Преобразование BGR в RGB
            image = Image.fromarray(image)  # Преобразование в формат PIL
            image = ImageTk.PhotoImage(image)  # Конвертация в PhotoImage для отображения в Tkinter

            self.static_image_display.config(image=image)
            self.static_image_display.image = image  # Сохранение ссылки на изображение

    def show_processed_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Преобразование BGR в RGB
        image = Image.fromarray(image)  # Преобразование в формат PIL
        image = ImageTk.PhotoImage(image)  # Конвертация в PhotoImage для отображения в Tkinter

        self.processed_image_display.config(image=image)
        self.processed_image_display.image = image  # Сохранение ссылки на изображение

    def apply_median_filter(self):
        if self.original_image is not None:
            median_filtered = cv2.medianBlur(self.original_image, 5)
            self.show_processed_image(median_filtered)

    def apply_linear_contrast(self):
        if self.original_image is not None:
            low_in = np.percentile(self.original_image, 5)  # Нижний порог входного диапазона
            high_in = np.percentile(self.original_image, 95)  # Верхний порог входного диапазона
            low_out = 0  # Нижний порог выходного диапазона
            high_out = 255
            img_float = self.original_image.astype(np.float32)

            # Нормализуем изображение
            img_normalized = (img_float - low_in) / (high_in - low_in)

            # Применяем линейное растяжение
            img_stretched = low_out + img_normalized * (high_out - low_out)

            # Ограничиваем значения пикселей в диапазоне [0, 255]
            img_stretched = np.clip(img_stretched, 0, 255)
            self.show_processed_image(img_stretched.astype(np.uint8))

    def equalize_histogram(self):
        if self.original_image is not None:
            hsv_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_image)
            v_eq = cv2.equalizeHist(v)
            hsv_eq_image = cv2.merge((h, s, v_eq))
            histogram_equalized_image = cv2.cvtColor(hsv_eq_image, cv2.COLOR_HSV2BGR)
            self.show_processed_image(histogram_equalized_image)

    def histogram_equalization_rgb(self):
        # Разделяем на три канала (R, G, B)
        if self.original_image is not None:
            image_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            r, g, b = cv2.split(image_rgb)
            r_eq = cv2.equalizeHist(r)
            g_eq = cv2.equalizeHist(g)
            b_eq = cv2.equalizeHist(b)
            rez_image = cv2.cvtColor(cv2.merge((r_eq, g_eq, b_eq)), cv2.COLOR_RGB2BGR)
            self.show_processed_image(rez_image)

    def histogram_equalization_hsv(self):
        if self.original_image is not None:
            hsv_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_image)
            v_eq = cv2.equalizeHist(v)
            hsv_eq_image = cv2.merge((h, s, v_eq))
            histogram_equalized_image = cv2.cvtColor(hsv_eq_image, cv2.COLOR_HSV2BGR)
            self.show_processed_image(histogram_equalized_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessor(root)
    root.mainloop()
