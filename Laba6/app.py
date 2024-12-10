import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import matplotlib.pyplot as plt

# Вершины (vertices)
vertices = np.array([
    [0.5 / 2, -2.0 / 2, -1.5 / 2],
    [3.5 / 2, 4.0 / 2, -1.5 / 2],
    [5.5 / 2, 4.0 / 2, -1.5 / 2],
    [1.5 / 2, -4.0 / 2, -1.5 / 2],
    [-0.5 / 2, -2.0 / 2, -1.5 / 2],
    [-3.5 / 2, 4.0 / 2, -1.5 / 2],
    [-5.5 / 2, 4.0 / 2, -1.5 / 2],
    [-1.5 / 2, -4.0 / 2, -1.5 / 2],
    [0.5 / 2, -2.0 / 2, 1.5 / 2],
    [3.5 / 2, 4.0 / 2, 1.5 / 2],
    [5.5 / 2, 4.0 / 2, 1.5 / 2],
    [1.5 / 2, -4.0 / 2, 1.5 / 2],
    [-0.5 / 2, -2.0 / 2, 1.5 / 2],
    [-3.5 / 2, 4.0 / 2, 1.5 / 2],
    [-5.5 / 2, 4.0 / 2, 1.5 / 2],
    [-1.5 / 2, -4.0 / 2, 1.5 / 2],
])

# Рёбра (edges)
edges = [
    (0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (6, 7),
    (0, 4), (3, 7), (8, 9), (9, 10), (10, 11), (12, 13),
    (13, 14), (14, 15), (8, 12), (11, 15),
    (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15),
]


def draw_axes():
    """
    Отрисовка координатных осей.
    Ось X: красная
    Ось Y: зеленая
    Ось Z: синяя
    """
    glBegin(GL_LINES)

    # Ось X (красный)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)

    # Ось Y (зеленый)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)

    # Ось Z (синий)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)

    glEnd()
    # Сбрасываем цвет в белый, чтобы он не повлиял на другие элементы
    glColor3f(1, 1, 1)

# Создание матрицы вращения
def create_rotation_matrix(axis, angle):
    axis = np.array(axis) / np.linalg.norm(axis)
    x, y, z = axis
    c, s = np.cos(angle), np.sin(angle)
    r = 1 - c
    return np.array([
        [c + r * x * x, r * x * y - s * z, r * x * z + s * y],
        [r * y * x + s * z, c + r * y * y, r * y * z - s * x],
        [r * z * x - s * y, r * z * y + s * x, c + r * z * z],
    ])

# Функция отрисовки объекта
def draw_object(transformed_vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(transformed_vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    translation = np.zeros(3)
    rotation = np.eye(3)
    is_rotating = False
    last_mouse_pos = None
    scale = 1

    last_transformation_matrix = None
    transformed_vertices = vertices.copy()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    is_rotating = True
                    last_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Левая кнопка мыши
                    is_rotating = False
            elif event.type == pygame.MOUSEMOTION:
                if is_rotating and last_mouse_pos:
                    mouse_dx, mouse_dy = pygame.mouse.get_rel()
                    axis = np.array([mouse_dy, mouse_dx, 0])
                    angle = np.linalg.norm([mouse_dx, mouse_dy]) * 0.01
                    if angle > 0:
                        axis = axis.astype(float) / np.linalg.norm(axis)
                        rotation = create_rotation_matrix(axis, angle) @ rotation
            elif event.type == KEYDOWN:
                if event.key == K_UP:  # Перемещение вверх
                    translation[1] += 0.1
                elif event.key == K_DOWN:  # Перемещение вниз
                    translation[1] -= 0.1
                elif event.key == K_LEFT:  # Перемещение влево
                    translation[0] -= 0.1
                elif event.key == K_RIGHT:  # Перемещение вправо
                    translation[0] += 0.1
                elif event.key == K_w:  # Увеличение масштаба
                    scale += 0.1
                elif event.key == K_s:  # Уменьшение масштаба
                    scale = max(0.1, scale - 0.1)
                elif event.key == K_z:
                        for edge in edges:
                            x = [transformed_vertices[edge[0]][0], transformed_vertices[edge[1]][0]]
                            y = [transformed_vertices[edge[0]][1], transformed_vertices[edge[1]][1]]
                            plt.plot(x, y, 'b-', linewidth=1)
                        plt.xlabel("X-axis")  # Подпись для оси X
                        plt.ylabel("Y-axis")  # Подпись для оси Y
                        plt.axis('equal')
                        plt.grid(True)
                        plt.title("Projection Oxy")
                        plt.show()
                elif event.key == K_y:
                        for edge in edges:
                            x = [transformed_vertices[edge[0]][0], transformed_vertices[edge[1]][0]]
                            z = [transformed_vertices[edge[0]][2], transformed_vertices[edge[1]][2]]
                            plt.plot(x, z, 'b-', linewidth=1)
                        plt.xlabel("X-axis")  # Подпись для оси X
                        plt.ylabel("Z-axis")  # Подпись для оси Y
                        plt.axis('equal')
                        plt.grid(True)
                        plt.title("Projection Oxz")
                        plt.show()
                elif event.key == K_x:
                        for edge in edges:
                            z = [transformed_vertices[edge[0]][2], transformed_vertices[edge[1]][2]]
                            y = [transformed_vertices[edge[0]][1], transformed_vertices[edge[1]][1]]
                            plt.plot(y, z, 'b-', linewidth=1)
                        plt.xlabel("Y-axis")  # Подпись для оси X
                        plt.ylabel("Z-axis")  # Подпись для оси Y
                        plt.axis('equal')
                        plt.grid(True)
                        plt.title("Projection Oyz")
                        plt.show()

        # Формирование итоговой матрицы
        transformation_matrix = np.eye(4)
        transformation_matrix[:3, :3] = rotation * scale
        transformation_matrix[:3, 3] = translation

        if not np.array_equal(transformation_matrix, last_transformation_matrix):
            print("\nTransformation Matrix:")
            print(transformation_matrix)
            last_transformation_matrix = transformation_matrix

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_axes()
        transformed_vertices = np.dot(vertices, transformation_matrix[:3, :3].T) + transformation_matrix[:3, 3]

        draw_object(transformed_vertices)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
