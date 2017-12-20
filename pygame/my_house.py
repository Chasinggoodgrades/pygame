#Made by Chase Poland
#This Will be my DREAM house cuz ya
#This will also be super amazing

import pygame
import math

pygame.init()

'''window'''
SIZE = (1200, 800)
TITLE = "Dream House"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

'''clock'''
clock = pygame.time.Clock()
refresh_rate = 60

'''colors'''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)

done = False

#pygame.draw.rect(screen, GREEN, [
pygame.draw.rect(screen, RED, [400, 600, 200, 200])
pygame.draw.polygon(screen, BLUE, [[350, 600], [500, 500], [650, 600]])


pygame.display.flip()
