# -*- coding: cp1251 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init():
    pygame.init()

    # Встановлення розміру та властивостей вікна
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Встановлення перспективної проекції
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Переміщення камери вздовж осі Z
    glTranslatef(0.0, 0.0, -5)

def draw_cube():
    # Визначення координат вершин куба
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    # Визначення ребер куба
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    # Відображення граней куба
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Поворот куба навколо трьох осей
        glRotatef(1, 3, 1, 1)

        # Очистка буферів кольору та глибини
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Відображення куба
        draw_cube()

        # Оновлення вікна
        pygame.display.flip()

        # Затримка для забезпечення потрібної кількості кадрів в секунду
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
