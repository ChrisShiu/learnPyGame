# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
from sys import exit

background_image = 'sushiplate.jpg'
mouse_image = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("这是什么Fucking游戏")

backround = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert.alpha()

while True:
	for event in pygame.ecent.get():
		if event.type == QUIT:
			exit()
	screen.blit(backround, (0,0))
	x, y = pygame.mouse.get_pos()
	x-= mouse_cursor.get_width() / 2
	y-= mouse_cursor.gei_height() / 2
	screen.blit(mouse_cursor, (x,y))
	pygame.display.update()