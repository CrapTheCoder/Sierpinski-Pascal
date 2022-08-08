from math import floor, ceil

import ctypes
from time import sleep

import pygame

user32 = ctypes.windll.user32
WINDOW_SIZE = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
HMID = WINDOW_SIZE[0] // 2

clock = pygame.time.Clock()

pygame.font.init()

finished = False
display = pygame.display.set_mode(WINDOW_SIZE)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
WHITE = (255, 255, 255)
X1 = (100, 100, 100)
X2 = (200, 200, 200)

COLOR_LIST = [(242, 122, 80), (84, 91, 162), (252, 241, 73)]

triangle = [[1]]

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    display.fill(BLACK)

    SQUARE_SIZE = WINDOW_SIZE[1] / len(triangle)

    for row_index, row in enumerate(triangle):
        for col_index, col in enumerate(row):
            pygame.draw.rect(display, COLOR_LIST[triangle[row_index][col_index] % 3], (
                ceil(HMID - (col_index - len(row) // 2) * SQUARE_SIZE - (SQUARE_SIZE / 2) * (row_index % 2 + 1)),
                ceil(row_index * SQUARE_SIZE),
                ceil(SQUARE_SIZE),
                ceil(SQUARE_SIZE)
            ))

    triangle.append([1] + [triangle[-1][i] + triangle[-1][i + 1] for i in range(len(triangle[-1]) - 1)] + [1])
    sleep(0.02)

    pygame.display.update()
