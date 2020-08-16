# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 4096

# create the game of life object
life = conway.GameOfLife(N)
# life.insertBlinker((0,0))
# life.insertGlider((0,0))
# life.insertGliderGun((0,0))
# life.insertFromFile("dragon spaceship.cells", (0,100))
# life.insertFromFile("ak94 gun.cells", (100,100))
# life.insertFromFile("vacuumgun gun.cells", (100,100))
# life.insertFromFile("stargate oscillator.cells", (100,100))
# life.insertFromFile("7enginecordership spaceship.cells", (100,100))
life.insertFromFile("3enginecordership gun 279x258.cells", (100, 100))
cells = life.getStates()  # initial state

# In a cellular automaton, a gun is a pattern with a main part that repeats periodically, like an oscillator,
# and that also periodically emits spaceships. but here the gun is not emit periodically and the left end did not work.
# -------------------------------
# plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)


def animate(i):
    """perform animation step"""
    global life

    life.evolve()
    cells_updated = life.getStates()

    img.set_array(cells_updated)

    return img,


interval = 50  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True, repeat=True)

plt.show()
