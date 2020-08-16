# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 2 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from turing_machine import TuringMachine

# Python generators are useful for Turing machines because they invert control
# over to the caller. They can generate an output stream lazily
# Iterators allow lazy evaluation, only generating the next element of an iterable object when requested.
# This is useful for very large data sets.
#
# EXAMPLE:
# >>> x = (i ** 2 for i in range(1, 10))
# >>> next(x)
# 1
# >>> next(x)
# 4
# >>> next(x)
# 9
#
# This means that you could construct a Turing Machine lazily, repeatedly
# ask for output with next, _only when needed_, or collect all its outputs
# if needed
#
# EXAMPLE:
# >>> x = (i ** 2 for i in range(1, 10))
# >>> list(x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81
# generator could write a function that
#         potentially runs forever and it's up the the caller to decide how many
#         steps are executed. We give the user control to execute us one step at a time. This
#         is what Python generators are (partially) for. The yield expression
#         suspends us and gives controll to the caller until he or she decides to
#         resume our execution.
# Because execution is done in a generator, it’s possible to have infinite executions
#         but the acceptance checks are limited by the number of steps they are allowed to perform.

#create the Turing machine
bbeaver2 = TuringMachine(
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.

        # make turn 1 move right turn 1 move right
        # then keep move left turn 1 move left turn 1 move left then halt at state b with 1
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver3 = TuringMachine(
    {
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('c', '1', 'L'),
        ('b', '0'): ('c', '0', 'R'),
        ('b', '1'): ('c', '1', 'R'),
        ('c', '0'): ('a', '1', 'L'),
        ('c', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver4 = TuringMachine(
    {
        ('a', '0'): ('b', '1', 'R'),   # <- start here
        ('a', '1'): ('h', '1', 'L'),
        ('b', '0'): ('c', '1', 'R'),   # add 1
        ('b', '1'): ('b', '1', 'L'),
        ('c', '0'): ('d', '0', 'R'),   # keep 0
        ('c', '1'): ('d', '0', 'L'),
        ('d', '0'): ('a', '1', 'L'),   # go back to turn 0 to 1
        ('d', '1'): ('d', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver5 = TuringMachine(
    {
        # ('a', '0'): ('b', '1', 'L'),
        # ('a', '1'): ('a', '1', 'L'),
        # ('b', '0'): ('c', '1', 'R'),
        # ('b', '1'): ('b', '1', 'R'),
        # ('c', '0'): ('a', '1', 'L'),
        # ('c', '1'): ('d', '1', 'R'),
        # ('d', '0'): ('a', '1', 'L'),
        # ('d', '1'): ('e', '1', 'R'),
        # ('e', '0'): ('h', '1', 'R'),
        # ('e', '1'): ('c', '0', 'R'),     # normal busy

        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '1', 'R'),  # see 1 go right
        ('c', '0'): ('d', '1', 'R'),    # see 0 turn 0 to 1 and go right
        ('c', '1'): ('d', '1', 'R'),  # see 1 go right
        ('d', '0'): ('e', '1', 'R'),    # see 0 turn 0 to 1 and go right
        ('d', '1'): ('c', '1', 'R'),  # see 1 go right
        ('e', '0'): ('h', '1', 'R'),
        ('e', '1'): ('0', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

if __name__ == "__main__":
    def run(input_):
        w = input_
        # the same as mine 4 ones
        # This is an optimal BB-2. 4 is the maximum number of 1s you can get for 2 states
        print("BB with 2 states")
        bbeaver2.debug(w, step_limit=1000)
        print()
        # 6
        print("BB with 3 states")
        bbeaver3.debug(w, step_limit=1000)
        print()
        # 13
        print("BB with 4 states")
        bbeaver4.debug(w, step_limit=1000)
        print()
        # This machine runs for 47176870 steps, writing 4098 1s, and then halts. So BB(5) is at least 47176870
        print("BB with 5 states")
        bbeaver5.debug(w, step_limit=1000)
        print()
        # The busy beaver function is defined so that
        # \Sigma(n) = max { \sigma(M) | M is a halting n-state 2-symbol Turing machine}
        # The maximum is unique if it exists, which it does (Rado proved this). This is just a number.
        #
        # Therefore \Sigma(n) is also unique, and so the discrete function \Sigma: N --> N is also unique.
        # The busy beaver function is a function which tells you the maximum score for all n-state Turing machines.
        # There is only one function. However, there are multiple Turing machines which attain this maximum
        # [4(n+1)]^2n so 5 state have 24^10 different TM with 5 states. (for each nonhalting state, there are two
        # transitions out, so there are 2n total transitions, and each transition have 2 possibilities for the symbol
        # being written, 2 possibilities for the direction to move - left or right, and (n+1) possibilities for what
        # states to go - including the halting state)

        # if we can calculate BB(n), we can solve the halting problem by converting the input program to
        # a machine of the required type and determining its size n, calculating BB(n) and running the machine.
        # If it runs more than BB(n) steps, then, by definition, it must run forever.

    run('00000000000000')  # 14 0

# bbeaver.debug('00000000000000', step_limit=1000)
