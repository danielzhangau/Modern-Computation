# -*- coding: utf-8 -*-

import conway
import pygame
import numpy as np
N = 300

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((0,0))
#life.insertGliderGunFixed((0,0))
# life.insertFromFile("snail spaceship.cells", (0,30))
# life.insertFromFile("dragon spaceship.cells", (0,30))
# life.insertFromFile("ak94 gun.cells", (0,0))
life.insertFromFile("vacuumgun gun.cells", (0,0))
cells = life.getStates() #initial state

#-------------------------------
#plot cells
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation


pygame.init()
screen = pygame.display.set_mode((N,N))
surface = pygame.surfarray.make_surface(np.swapaxes(cells, 0, 1))
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.blit(surface, (0,0))
    pygame.display.flip()
    life.evolve()
    cells = life.getStates()
    surface = pygame.surfarray.make_surface(np.swapaxes(cells, 0, 1))
pygame.quit()