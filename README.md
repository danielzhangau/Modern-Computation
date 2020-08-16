# Theory-of-Computing
UQ COMP2048 Python

## Lab1: Code Breaking
The Caesar cipher is a simple plain text substitution cipher, where you replace your message alphabets to the same alphabet but shifted by a constant offset.

## Lab2: Turing Machine Simulator
In this laboratory, we will create Turing machines based on a Python simulator and program them using transition rules. The Python Turing machine simulator runs with a single sided infinite tape designed using Python generators. We will also be able to print the configuration of the machine during computation to debug and implement the algorithms requested in the following parts of the laboratory.

The [Busy Beaver game](https://en.wikipedia.org/wiki/Busy_Beaver_game) is creating a halting, binary alphabet Turing machine that writes the greatest number of ones on its tape using a limited number of states (or cards) plus an accept or halt state. Each card usually represents a state and its transitions based on the alphabet character encountered.
## Lab3: Game of Life
The [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) (GoL) simulation is a [cellular automation](https://en.wikipedia.org/wiki/Cellular_automaton) originally developed by John Conway. The game involves a set of cells within an 𝑁𝑁×𝑁𝑁 grid whose state is either alive or dead (i.e. 0 or 1 respectively). The grid effectively represents the ‘universe’ that will be simulated and the alive cells the life within it. The game is governed by a set of simple rules that dictate the next state of each cell in this universe depending on its current state and the states of its neighbours. The rules of GoL depend on the 8-connected neighbours of a cell as follows:
1. Underpopulation: A live cell that has < 2 live neighbouring cells will die
2. Survival: A live cell that has 2-3 live neighbouring cells will remain alive
3. Overpopulation: A live cell with more than 3 live neighbours will die
4. Reproduction: A dead cell with exactly 3 live neighbours will become alive
The game begins with an initial state of the universe with a pattern of live cells. The universe is evolved by applying the above rules to each cell of the universe to determine the next iteration of the simulation. The evolution of the universe is observed by continual computing the next iteration of the universe. See chapter 7, section 7.6.4 of (Moore and Mertens, 2011) for more theoretical details.
In this laboratory, we will create a simulation of the GoL using Python based on an initial class provided. In the following parts of the lab, we will be required to code up the algorithms related to the computation, importation and evaluation of the GoL.
one example pattern:
![example](https://github.com/danielzhangau/Theory-of-Computing/blob/master/3gameoflife%20lab/before.png)

[Langton’s Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) is a cellular automation that is Turing complete and is capable of chaotic behaviour. In this universe, a single ant is allowed to roam a space consisting of 𝑁𝑁 × 𝑁𝑁 squares according to a set of rules. There are various rules known, but one of the simplest ones is the following:
1. If on a white square, toggle the colour of the square and move to the square on the right.
2. If on a black square, toggle the colour of the square and move to the square on the left.
By toggling, we mean change the colour to the next colour in a given sequence. For a binary colour system, this is simply toggling between black and white.

# What I learned:
- The halting problem
- Finite State Machine implementation e.g. AI player
- Turing machine implementation e.g. busy beaver (State-based computation)
- Cellular machine implementation e.g. game of life and langton's ant (Chaotic machines from simple rules)
- lambda calculus (Computation from nothing but functions)
- quantum computation (Computation with the bizarre quantum properties of matter)
