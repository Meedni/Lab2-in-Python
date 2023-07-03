# -*- coding: cp1251 -*-
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import matplotlib.pyplot as plt


def init():
    pygame.init()

    # ������������ ������ �� ������������ ����
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # ������������ ������������ ��������
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # ���������� ������ ������ �� Z
    glTranslatef(0.0, 0.0, -5)

def draw_cube():
    # ���������� ��������� ������ ����
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

    # ���������� ����� ����
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

    # ³���������� ������ ����
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

        # ������� ���� ������� ����� ����
        glRotatef(1, 3, 1, 1)

        # ������� ������ ������� �� �������
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ³���������� ����
        draw_cube()

        # ��������� ����
        pygame.display.flip()

        # �������� ��� ������������ ������� ������� ����� � �������
        pygame.time.wait(10)

def compute_intersection(surface1, surface2):
    # ��������� ��� �������� ������ ���������
    # surface1 � surface2 - �� ���� ���� �������
    # ��������� ������� ���� ��� ��������, ������������� �� ����� �����

    # �������: ������ �'������ ��������� �� ������ ����� ���� ���������
    intersection = np.array([surface1[0], surface2[0], surface1[-1], surface2[-1]])

    return intersection

def visualize_intersection(intersection):
    # ³���������� ��� ��������

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # �������� ���������� ����� �� ����� ������ x, y, z
    x = intersection[:, 0]
    y = intersection[:, 1]
    z = intersection[:, 2]

    # ³��������� ��� ��������
    ax.plot(x, y, z, color='red', label='Intersection')

    # ��������� ������������ �������
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    # �������� ������
    plt.show()

# ������� ������������
surface1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # ����������, �� �� ����� ����� ��������
surface2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])  # ����������, �� �� ����� ����� ��������

intersection = compute_intersection(surface1, surface2)
visualize_intersection(intersection)

if __name__ == '__main__':
    main()
