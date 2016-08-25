# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *

background_image = r'D:\test\learnPyGame\world.png'
mouse_image = r'D:\test\learnPyGame\2.png'
running = True

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("红红火火恍恍惚惚")

background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

	screen.blit(background, (0,0))
	x, y = pygame.mouse.get_pos()
	pygame.mouse.set_visible(False)
	x-= mouse_cursor.get_width() / 2
	y-= mouse_cursor.get_height() / 2
	screen.blit(mouse_cursor, (x,y))
	pygame.display.update()