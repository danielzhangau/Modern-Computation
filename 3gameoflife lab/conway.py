# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal, ndimage


class GameOfLife:
    """
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    """

    def __init__(self, N=256, finite=False, fastMode=True):
        self.grid = np.zeros((N, N), np.uint)
        self.neighborhood = np.ones((3, 3), np.uint)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.rows = N  # use for slow implementation of evolve
        self.cols = N  # use for slow implementation of evolve

    def getStates(self):
        """
        Returns the current states of the cells
        """
        return self.grid

    def getGrid(self):
        """
        Same as getStates()
        """
        return self.getStates()

    def evolve(self):
        """
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        """
        # The Fourier transform method has order O(NlogN) while the direct method has order O(N^2).
        # An FFT rapidly computes such transformations by factorizing the DFT matrix into a product of sparse
        # (mostly zero) factors. As a result, it manages to reduce the complexity of computing the DFT from
        # O(N^2), which arises if one simply applies the definition of DFT, to O(NlogN), where N is the data size.

        if self.fastMode:
            neighbors = signal.convolve2d(
                self.grid,  # in1
                self.neighborhood,  # in2
                mode='same',  # The output is the same size as in1, centered with respect to the ‘full’ output.
                boundary='fill',
                fillvalue=0  # Value to fill pad input arrays with.
            )
            # if (center == self.aliveValue and alive == 2) or (alive == 3):
            self.grid = np.logical_or(np.logical_and(self.grid, np.equal(neighbors, 2))
                                      , np.equal(neighbors, 3)).astype(np.uint)
        else:
            # implement the GoL rules by thresholding the weights
            def evolve_cell(footprint):
                # generic_filter passes all values covered by a structuring element as a flat array,
                center = footprint[4]  # from left to right from top to bottom index start with 0
                footprint[4] = 0  # do not count centre pixel
                # get weighted sum of neighbors
                alive = np.sum(footprint)

                # Any live cell with two or three live neighbours survives.
                # Any dead cell with three live neighbours becomes a live cell.
                if (center == self.aliveValue and alive == 2) or (alive == 3):
                    return 1
                # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                return 0

            # update the grid by using generic_filter
            # Typically, a filter is used to iterate a “selector” (called a structuring element) over an array,
            # compute some function of all the values covered by the structuring element,
            # and replace the central value by the output of the function.
            self.grid = ndimage.generic_filter(
                input=self.grid,
                function=evolve_cell,
                # equivalent to size=(3,3)
                # equivalent to footprint=np.array([[1,1,1],[1,1,1],[1,1,1]]),
                footprint=np.ones((3, 3), np.uint),
                # The mode parameter determines how the array borders are handled,
                mode="constant",
                # value to fill past edges of input if mode is 'constant'. Default is 0.0
                cval=self.deadValue
            )

            ### tried but not working properly ###
            # newGrid = np.zeros((self.rows, self.cols), np.uint)
            # for i in range(self.rows):
            #     for j in range(self.cols):
            #         alive_neighbors = 0
            #         for a in range(3):
            #             for b in range(3):
            #                 if a != 1 and b != 1:
            #                     neigh = self.grid.item(i % self.rows, j % self.cols)
            #                     self.neighborhood[i][j] = neigh
            #         alive_neighbors = np.sum(self.neighborhood)
            #         center = self.grid.item(i,j)
            #         if (center == self.aliveValue and alive_neighbors == 2) or (alive_neighbors == 3):
            #             newGrid.itemset((i,j), self.aliveValue)
            #         # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            #         newGrid.itemset((i,j), self.deadValue)
            # self.grid = newGrid

    def insertBlinker(self, index=(0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0] + 1, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 5, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 23] = self.aliveValue

        self.grid[index[0] + 6, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 19] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 7, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 17] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 15] = self.aliveValue

    def insertFromFile(self, filename, index=((0, 0))):
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            start_lines = [i for i in lines if not i.startswith("!")]

            for (x, line) in enumerate(start_lines):
                for (y, cell) in enumerate(line):
                    if cell == 'O':
                        self.grid[index[0] + x, index[1] + y] = self.aliveValue
                    else:
                        self.grid[index[0] + x, index[1] + y] = self.deadValue
