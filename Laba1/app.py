import tkinter as tk
from tkinter import colorchooser

# Конвертация RGB в CMYK
def rgb_to_cmyk(r, g, b):
    r /= 255
    g /= 255
    b /= 255
    k = 1 - max(r, g, b)
    if k == 1:
        c = m = y = 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    return int(c * 255), int(m * 255), int(y * 255), int(k * 255)

# Конвертация CMYK в RGB
def cmyk_to_rgb(c, m, y, k):
    r = 255 * (1 - c / 255) * (1 - k / 255)
    g = 255 * (1 - m / 255) * (1 - k / 255)
    b = 255 * (1 - y / 255) * (1 - k / 255)
    return int(r), int(g), int(b)

def rgb_to_hsl(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    l = (cmax + cmin) / 2

    if delta == 0:
        h = s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

        if cmax == r:
            h = ((g - b) / delta) % 6
        elif cmax == g:
            h = (b - r) / delta + 2
        elif cmax == b:
            h = (r - g) / delta + 4

        h *= 60

        if h < 0:
            h += 360

    return (int(h), int(s * 100), int(l * 100))

def hsl_to_rgb(h, s, l):
    s /= 100.0
    l /= 100.0

    if s == 0:
        r = g = b = int(l * 255)
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q

        r = int(hue_to_rgb(p, q, h / 360 + 1/3) * 255)
        g = int(hue_to_rgb(p, q, h / 360) * 255)
        b = int(hue_to_rgb(p, q, h / 360 - 1/3) * 255)

    return (r, g, b)

# Обновление цвета квадрата и отображаемых значений
def update_color():
    if color_mode.get() == 'RGB':
        r = rgb_scale_r.get()
        g = rgb_scale_g.get()
        b = rgb_scale_b.get()
        c, m, y, k = rgb_to_cmyk(r, g, b)
        h, s, l = rgb_to_hsl(r, g, b)
    elif color_mode.get() == 'HSL':
        h = hsl_scale_h.get()
        s = hsl_scale_s.get()
        l = hsl_scale_l.get()
        r, g, b = hsl_to_rgb(h, s, l)
        c, m, y, k = rgb_to_cmyk(r, g, b)
    else:  # CMYK
        c = cmyk_scale_c.get()
        m = cmyk_scale_m.get()
        y = cmyk_scale_y.get()
        k = cmyk_scale_k.get()
        r, g, b = cmyk_to_rgb(c, m, y, k)
        h, s, l = rgb_to_hsl(r, g, b)

    # Обновление цвета квадрата
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    square.config(bg=color_hex)

    # Обновление значений на ползунках и в полях ввода
    cmyk_scale_c.set(c)
    cmyk_scale_m.set(m)
    cmyk_scale_y.set(y)
    cmyk_scale_k.set(k)
    hsl_scale_h.set(h)
    hsl_scale_l.set(l)
    hsl_scale_s.set(s)
    rgb_scale_r.set(r)
    rgb_scale_g.set(g)
    rgb_scale_b.set(b)

    entry_r.delete(0, tk.END); entry_r.insert(0, r)
    entry_g.delete(0, tk.END); entry_g.insert(0, g)
    entry_b.delete(0, tk.END); entry_b.insert(0, b)

    entry_h.delete(0, tk.END); entry_h.insert(0, h)
    entry_s.delete(0, tk.END); entry_s.insert(0, s)
    entry_l.delete(0, tk.END); entry_l.insert(0, l)

    entry_c.delete(0, tk.END); entry_c.insert(0, c)
    entry_m.delete(0, tk.END); entry_m.insert(0, m)
    entry_y.delete(0, tk.END); entry_y.insert(0, y)
    entry_k.delete(0, tk.END); entry_k.insert(0, k)

def choose_color():
    color_code = colorchooser.askcolor(title="Choose RGB Color")
    if color_code[0]:
        r, g, b = [int(c) for c in color_code[0]]
        if color_mode.get() == 'RGB':
            rgb_scale_r.set(r)
            rgb_scale_g.set(g)
            rgb_scale_b.set(b)
        elif color_mode.get() == 'HSL':
            h, s, l = rgb_to_hsl(r, g, b)
            hsl_scale_h.set(h)
            hsl_scale_s.set(s)
            hsl_scale_l.set(l)
        else:
            c, m, y, k = rgb_to_cmyk(r, g, b)
            cmyk_scale_c.set(c)
            cmyk_scale_m.set(m)
            cmyk_scale_y.set(y)
            cmyk_scale_k.set(k)
        update_color()

# Обработка изменения значения Scale через Entry
def update_from_entry(scale_var, entry_var):
    try:
        value = int(entry_var.get())
        scale_var.set(value)
        update_color()
    except ValueError:
        pass

# Переключение между режимами
def toggle_mode_1():
    if color_mode.get() == 'RGB':
        color_mode.set('CMYK')
        rgb_frame.pack_forget()
        cmyk_frame.pack()
        button_toggle_mode1.config(text='HSL')
        button_toggle_mode2.config(text='RGB')
    elif color_mode.get() == 'CMYK':
        color_mode.set('HSL')
        cmyk_frame.pack_forget()
        hsl_frame.pack()
        button_toggle_mode1.config(text='RGB')
        button_toggle_mode2.config(text='CMYK')
    else:  # HSL
        color_mode.set('RGB')
        hsl_frame.pack_forget()
        rgb_frame.pack()
        button_toggle_mode1.config(text='CMYK')
        button_toggle_mode2.config(text='HSL')

def toggle_mode_2():
    if color_mode.get() == 'RGB':
        color_mode.set('HSL')
        rgb_frame.pack_forget()
        hsl_frame.pack()
        button_toggle_mode1.config(text='RGB')
        button_toggle_mode2.config(text='CMYK')
    elif color_mode.get() == 'CMYK':
        color_mode.set('RGB')
        cmyk_frame.pack_forget()
        rgb_frame.pack()
        button_toggle_mode1.config(text='CMYK')
        button_toggle_mode2.config(text='HSL')
    else:  # HSL
        color_mode.set('CMYK')
        hsl_frame.pack_forget()
        cmyk_frame.pack()
        button_toggle_mode1.config(text='HSL')
        button_toggle_mode2.config(text='RGB')

def validate_input(char):
    return char.isdigit()

# Создаем главное окно
root = tk.Tk()
root.title("Color Model Converter")
root.geometry("900x600")
root.configure(bg="#f4f4f4")

# Переключатель между моделями
color_mode = tk.StringVar(value='RGB')

#Label of current mode
label_mode = tk.Label(root, textvariable= color_mode, font=("Arial", 14))

#validator
vcmd = (root.register(validate_input), '%S')

# Создаем фреймы для RGB и CMYK и HSL
rgb_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
cmyk_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
hsl_frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
button_frame = tk.Frame(root, padx=10, pady=10)

# Ползунки и поля ввода для RGB
rgb_scale_r = tk.Scale(rgb_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                        label='Red', command=lambda _: update_color(), bg="#ffffff")
entry_r = tk.Entry(rgb_frame)
entry_r.config(validate='key', validatecommand=vcmd)
entry_r.bind("<KeyRelease>", lambda event: update_from_entry(rgb_scale_r, entry_r))

rgb_scale_g = tk.Scale(rgb_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                        label='Green', command=lambda _: update_color(), bg="#ffffff")
entry_g = tk.Entry(rgb_frame)
entry_g.config(validate='key', validatecommand=vcmd)
entry_g.bind("<KeyRelease>", lambda event: update_from_entry(rgb_scale_g, entry_g))

rgb_scale_b = tk.Scale(rgb_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                        label='Blue', command=lambda _: update_color(), bg="#ffffff")
entry_b = tk.Entry(rgb_frame)
entry_b.config(validate='key', validatecommand=vcmd)
entry_b.bind("<KeyRelease>", lambda event: update_from_entry(rgb_scale_b, entry_b))

# Ползунки и поля ввода для CMYK
cmyk_scale_c = tk.Scale(cmyk_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                         label='Cyan', command=lambda _: update_color(), bg="#ffffff")
entry_c = tk.Entry(cmyk_frame)
entry_c.config(validate='key', validatecommand=vcmd)
entry_c.bind("<KeyRelease>", lambda event: update_from_entry(cmyk_scale_c, entry_c))

cmyk_scale_m = tk.Scale(cmyk_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                         label='Magenta', command=lambda _: update_color(), bg="#ffffff")
entry_m = tk.Entry(cmyk_frame)
entry_m.config(validate='key', validatecommand=vcmd)
entry_m.bind("<KeyRelease>", lambda event: update_from_entry(cmyk_scale_m, entry_m))

cmyk_scale_y = tk.Scale(cmyk_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                         label='Yellow', command=lambda _: update_color(), bg="#ffffff")
entry_y = tk.Entry(cmyk_frame)
entry_y.config(validate='key', validatecommand=vcmd)
entry_y.bind("<KeyRelease>", lambda event: update_from_entry(cmyk_scale_y, entry_y))

cmyk_scale_k = tk.Scale(cmyk_frame, from_=0, to=255, orient=tk.HORIZONTAL,
                         label='Black', command=lambda _: update_color(), bg="#ffffff")
entry_k = tk.Entry(cmyk_frame)
entry_k.config(validate='key', validatecommand=vcmd)
entry_k.bind("<KeyRelease>", lambda event: update_from_entry(cmyk_scale_k, entry_k))
cmyk_scale_k.set(255)
entry_k.insert(0, str(255))

# Ползунки и поля ввода для HSL
hsl_scale_h = tk.Scale(hsl_frame, from_=0, to=360, orient=tk.HORIZONTAL,
                        label='Hue', command=lambda _: update_color(), bg="#ffffff")
entry_h = tk.Entry(hsl_frame)
entry_h.config(validate='key', validatecommand=vcmd)
entry_h.bind("<KeyRelease>", lambda event: update_from_entry(hsl_scale_h, entry_h))

hsl_scale_s = tk.Scale(hsl_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                        label='Saturation', command=lambda _: update_color(), bg="#ffffff")
entry_s = tk.Entry(hsl_frame)
entry_s.config(validate='key', validatecommand=vcmd)
entry_s.bind("<KeyRelease>", lambda event: update_from_entry(hsl_scale_s, entry_s))

hsl_scale_l = tk.Scale(hsl_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                        label='Lightness', command=lambda _: update_color(), bg="#ffffff")
entry_l = tk.Entry(hsl_frame)
entry_l.config(validate='key', validatecommand=vcmd)
entry_l.bind("<KeyRelease>", lambda event: update_from_entry(hsl_scale_l, entry_l))

# Кнопка для переключения режимов
button_toggle_mode1 = tk.Button(button_frame, text="CMYK", command=toggle_mode_1,
                                bg="#007bff", fg="white", font=("Arial", 12), padx=10)
button_toggle_mode2 = tk.Button(button_frame, text="HSL", command=toggle_mode_2,
                                bg="red", fg="white", font=("Arial", 12), padx=10)
button_choose_color = tk.Button(root, text="Choose Color", command=choose_color,
                                bg="green", fg="white", font=("Arial", 12), padx=10)

#Оповещение о режиме
label_toggle = tk.Label(button_frame, text="Toggle to:", font=("Arial", 14),)

# Квадрат для отображения цвета
square = tk.Label(root, width=50, height=25, bg = "black")

# Располагаем элементы на окне RGB
label_toggle.pack(pady=5)
button_frame.pack(pady=5)
button_toggle_mode1.pack( side=tk.LEFT)
button_toggle_mode2.pack( side=tk.LEFT)
label_mode.pack(pady=5)


square.pack(pady=20)

rgb_frame.pack()

rgb_scale_r.pack(side=tk.LEFT)
entry_r.pack(side=tk.LEFT)
rgb_scale_g.pack(side=tk.LEFT)
entry_g.pack(side=tk.LEFT)
rgb_scale_b.pack(side=tk.LEFT)
entry_b.pack(side=tk.LEFT)

# Располагаем элементы на окне CMYK
cmyk_frame.pack_forget()  # Скрываем CMYK фрейм изначально

cmyk_scale_c.pack(side=tk.LEFT)
entry_c.pack(side=tk.LEFT)
cmyk_scale_m.pack(side=tk.LEFT)
entry_m.pack(side=tk.LEFT)
cmyk_scale_y.pack(side=tk.LEFT)
entry_y.pack(side=tk.LEFT)
cmyk_scale_k.pack(side=tk.LEFT)
entry_k.pack(side=tk.LEFT)

# Располагаем элементы на окне HSL
hsl_frame.pack_forget()  # Скрываем HSL фрейм изначально

hsl_scale_h.pack(side=tk.LEFT)
entry_h.pack(side=tk.LEFT)
hsl_scale_s.pack(side=tk.LEFT)
entry_s.pack(side=tk.LEFT)
hsl_scale_l.pack(side=tk.LEFT)
entry_l.pack(side=tk.LEFT)

button_choose_color.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()
