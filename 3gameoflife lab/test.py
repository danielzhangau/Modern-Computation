import random
import time

UP = [0, 1]
DOWN = [0, -1]
LEFT = [-1, 0]
RIGHT = [1, 0]

directions = [UP, DOWN, LEFT, RIGHT]

def rotate_clockwise(vec):
    return [ vec[1], -vec[0] ]

def rotate_counterclock(vec):
    return [ -vec[1], vec[0] ]

class LangtonAnt:
    """
        Langton's Ant Simulator
    """

    BLACK = 0
    WHITE = 1
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [ [ LangtonAnt.WHITE for j in range(self.grid_size) ] for i in range(self.grid_size)  ]
        self._initialize_ant(grid_size)

    def _initialize_ant(self, size):
        self.ant_r, self.ant_c = int(self.grid_size/2), int(self.grid_size/2)
        # randomize initial direction
        self.direction = random.choice(directions)
        print(self.direction)

    def run(self, epoch=10):
        for i in range(epoch):
            print("Epoch ==> {} :: BLACK:0 :: WHITE:1".format(i))
            print("="*40)
            print(self)
            self.step()
            time.sleep(0.1)
            print("="*40)
        print("Final state...")
        print("="*40)
        print(self)

    def step(self):
        """
            Run for single time step.
            Transition from time t to (t+1)
        """
        r, c = self.ant_r, self.ant_c
        if self.grid[r][c] == LangtonAnt.WHITE:
            self.direction = rotate_counterclock(self.direction)
            self.grid[r][c] = LangtonAnt.BLACK
        else:
            self.direction = rotate_clockwise(self.direction)
            self.grid[r][c] = LangtonAnt.WHITE

        self.ant_r -= self.direction[1]
        self.ant_c += self.direction[0]

    def __str__(self):
        r, c = self.ant_r, self.ant_c
        curr = self.grid[r][c]
        self.grid[r][c] = '*'
        ret = ""
        for row in self.grid:
            for x in row:
                ret += str(x) + " "
            ret += "\n"
        self.grid[r][c] = curr
        return ret.strip()

def main():
    ant = LangtonAnt(25)
    ant.run(500)


# -------------------------------
# plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True, cmap='tab20c', vmin=0, vmax=(len(ruleset) - 1))


def animate(i):
    """perform animation step"""
    global ant

    ant.evolve()
    cells_updated = ant.get_states()

    img.set_array(cells_updated)

    return img,


interval = 0.1  # ms - run it as fast as possible# ruleset = ant.CHAOTIC

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True, repeat=True)

plt.show()