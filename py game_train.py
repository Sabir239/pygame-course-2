import pygame
from sys import exit
pygame.init()
#draw screen and title
screen = pygame.display.set_mode((800,600))
title = pygame.display.set_caption('uncunu')
#import image for the soul
caje = pygame.image.load('Caja.png')
#color
black = (0,0,0)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()
    pygame.display.update()
    #draw the caje in position:
    screen.blit(caje,(200,150))
    clock.tick(240)