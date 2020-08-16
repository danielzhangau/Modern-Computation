# -*- coding: utf-8 -*-
"""
Game of life simple script for checking init states and checking if the evolution is
implemented correctly.

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 64

# create the game of life object
life = conway.GameOfLife(N)
# life.insertBlinker((0,0))
life.insertGlider((0,0))        # It travels diagonally across the Life grid at a speed of c/4
# life.insertGliderGun((0,0))     # Gosper glider gun consists of two queen bee shuttles stabilized by two blocks.
# life.insertFromFile("snail spaceship.cells", (0,30))
# life.insertFromFile("dragon spaceship.cells", (0,30))
# life.insertFromFile("ak94 gun.cells", (0,0))
# life.insertFromFile("vacuumgun gun.cells", (0,0))
# life.insertFromFile("stargate oscillator.cells", (0,0))
# life.insertFromFile("7enginecordership spaceship.cells", (0,0))
cells = life.getStates()  # initial state

# evolve once
life.evolve()
cellsUpdated1 = life.getStates()

# evolve twice
life.evolve()
cellsUpdated2 = life.getStates()

# -------------------------------
# plot cells
import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=0)
plt.gray()
plt.imshow(cells)  # initial state
ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
# grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.figure(num=1)
plt.imshow(cellsUpdated1)  # evolve once
ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
# grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.figure(num=2)
plt.imshow(cellsUpdated2)  # evolve twice
ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
# grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.show()
