# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
from test_turing_machine_example1 import print_states

#create the Turing machine
# transitions = {
#         #Write your transition rules here as entries to a Python dictionary
#         #For example, the key will be a pair (state, character)
#         #The value will be the triple (next state, character to write, move head L or R)
#         #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
#         #then transition to state q1, write a 0 and move head right.
#         ('q0', '1'): ('SkipFirst', '', 'R'),
#         # We already have our first iteration; it's the accumulator
#         ('SkipFirst', '1'): ('SkipGlobalLoop', 'd', 'R'),
#         # 1 * x: Keep x and accept
#         ('SkipFirst', '0'): ('qa', '', 'R'),
#         ('SkipGlobalLoop', '1'): ('SkipGlobalLoop', '1', 'R'),
#         ('SkipGlobalLoop', '0'): ('MarkAccumulatorLoopIndex', '0', 'R'),
#         ('MarkAccumulatorLoopIndex', '1'): ('GetToEndOfAccAndMark', '*', 'R'),
#         ('GetToEndOfAccAndMark', '1'): ('GetToEndOfAccAndMark', '1', 'R'),
#         ('GetToEndOfAccAndMark', ''): ('GetToAccLoopIndexLeft', '#', 'L'),
#         ('MarkEndOfAcc', '1'): ('AddOne', '1', 'L'),
#         ('AddOne', '1'): ('GetToAccLoopIndexLeft', '1', 'L'),
#         ('GetToAccLoopIndexLeft', '1'): ('GetToAccLoopIndexLeft', '1', 'L'),
#         ('GetToAccLoopIndexLeft', '#'): ('GetToAccLoopIndexLeft', '#', 'L'),
#         ('GetToAccLoopIndexLeft', '*'): ('IncrAccLoopIndex', '1', 'R'),
#         ('IncrAccLoopIndex', '#'): ('GetToGlobalLoopIndex', '*', 'L'),
#         ('IncrAccLoopIndex', '1'): ('GetToEndOfAccAndAdd', '*', 'R'),
#         ('GetToEndOfAccAndAdd', '1'): ('GetToEndOfAccAndAdd', '1', 'R'),
#         ('GetToEndOfAccAndAdd', ''): ('GetToAccLoopIndexLeft', '1', 'L'),
#         ('GetToEndOfAccAndAdd', '#'): ('GetToEndOfAccAndAdd', '#', 'R'),
#         ('GetToGlobalLoopIndex', '1'): ('GetToGlobalLoopIndex', '1', 'L'),
#         ('GetToGlobalLoopIndex', '0'): ('GetToGlobalLoopIndex', '0', 'L'),
#         ('GetToGlobalLoopIndex', 'd'): ('IncrGlobalLoopIndex', '', 'R'),
#         ('GetToAccLoopIndexRight', '1'): ('GetToAccLoopIndexRight', '1', 'R'),
#         ('GetToAccLoopIndexRight', '0'): ('GetToAccLoopIndexRight', '0', 'R'),
#         ('GetToAccLoopIndexRight', '*'): ('GetToEndOfAccAndMark', '*', 'R'),
#         ('IncrGlobalLoopIndex', '1'): ('GetToAccLoopIndexRight', 'd', 'R'),
#         ('IncrGlobalLoopIndex', '0'): ('Cleanup', '1', 'R'),
#         ('Cleanup', '1'): ('Cleanup', '1', 'R'),
#         ('Cleanup', '*'): ('Cleanup', '1', 'R'),
#         ('Cleanup', ''): ('PruneLast', '', 'L'),
#         ('PruneLast', '1'): ('qa', '', 'R')
# }
# basically how the machine work is
#   - always skip the first 1 in the string then mark the following 1 as d and keep the rest 1 before 0
#   - then mark the first 1 after 0 as * e.g. d0*[1]1, then go end of the loop add #
#   - then go back * mark it back to 1, then mark the next 1 as *, then go end of the loop add 1
#   - until the * is mark back to 1 and next char is #, then go back to the d, run again for rest of the 1 before 0
#   - if no 1 bofore 0, then convert 0 to 1 and clean up any other symbol
#multiplier.debug('1101111', step_limit=300)

# alternative transition table able to calculate e.g 011111 (0 * 11111)
transitions = {
        #q0 is the starting state
        ('q0', '0'): ('times0', '0', 'R'),
        ('q0', '1'): ('q1', '1', 'R'),

        #q1 add a @ after the last bit to indicate where it ends
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '0'): ('q1', '0', 'R'),
        ('q1', ''): ('q2', '@', 'L'),

        #q2 check if there is 1 after 0 and before @, if no 1 is found go ql
        ('q2', 'X'): ('q2', 'X', 'L'),
        ('q2', '1'): ('q3', 'X', 'L'),
        ('q2', '0'): ('ql', '0', 'L'),

        #ql goes to the left most bit
        ('ql', 'X'): ('ql', 'X', 'L'),
        ('ql', '1'): ('ql', '1', 'L'),
        ('ql', '*'): ('ql', '*', 'L'),
        ('ql', '0'): ('ql', '0', 'L'),
        ('ql', '@'): ('ql', '@', 'L'),
        ('ql', ''): ('q4', '', 'R'),

        #q4 if no 1 is found between 0 and @, then eliminates every thing before @ and @ itself and accept
        ('q4', 'X'): ('q4', '', 'R'),
        ('q4', '1'): ('q4', '', 'R'),
        ('q4', '*'): ('q4', '', 'R'),
        ('q4', '0'): ('q4', '', 'R'),
        ('q4', '@'): ('qa', '', 'R'),
        ('q4', ''): ('qa', '', 'R'),#accept '' since there's case called times 0 state which will not have '@'

        #q3 check if the tape passes 0 sign in left direction
        ('q3', '1'): ('q3', '1', 'L'),
        ('q3', 'X'): ('q3', 'X', 'L'),
        ('q3', '@'): ('q3', '@', 'L'),
        ('q3', '0'): ('q5', '0', 'L'),

        #q5 '*' a 1 and go right with q6
        ('q5', '1'): ('q6', '*', 'R'),
        ('q5', '*'): ('q5', '*', 'L'),
        ('q5', ''): ('q7', '', 'R'),

        #q6 add a one to the right side of tape
        ('q6', '1'): ('q6', '1', 'R'),
        ('q6', '0'): ('q6', '0', 'R'),
        ('q6', '@'): ('q6', '@', 'R'),
        ('q6', '*'): ('q6', '*', 'R'),
        ('q6', 'X'): ('q6', 'X', 'R'),
        ('q6', ''): ('q3', '1', 'L'),

        #q7 means 1 times is finished, and go find the @ sign to do another times
        ('q7', ''): ('q7', '', 'R'),
        ('q7', '1'): ('q7', '1', 'R'),
        ('q7', '*'): ('q7', '1', 'R'),
        ('q7', '0'): ('q7', '0', 'R'),
        ('q7', 'X'): ('q7', 'X', 'R'),
        ('q7', '@'): ('q2', '@', 'L'),

        #times0 is the special case that no one is found before 0, then outcome equals 0
        ('times0', '1'): ('ql', '1', 'L')
}
if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w, step_limit=1000)

        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 111111

    # SHOULD ACCEPT
    run("11101111")
    # outputs 111111111111

    run("01111")
