# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
from test_turing_machine_example1 import print_states

#create the Turing machine
transitions = {
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        ('q0', '1'):('skipFirst','1','R'),
        ('skipFirst', '1'):('skipFirst','1','R'),
        ('skipFirst', '0'):('skipSecond','1','R'),
        ('skipSecond', '1'):('skipSecond','1','R'),
        ('skipSecond', ''): ('PruneLast', '', 'L'),
        ('PruneLast', '1'): ('qa', '', 'R'),
}
# This machine matches identical strings of characters at either end of the delimiter, and transforms them into Xs
# computation:
#   - run ('q0', '1'), it mean the string must start with 1, otherwise reject
#   - if satisfy it move to 'skipFirst' state and read next char if it's 1, stay same and move right,
#   - or if it's 0, turn to 1 and go state skipSecond, then keep reading the 1 stay same
#   - until ('skipSecond', '') is reached, it go state PruneLast
#   - and convert the last 1 to a 0
#   (note: there should only have one zero, otherwise reject)

if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w)
        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 11111

    # SHOULD ACCEPT
    run("11101111")
    #     # outputs 1111111
    run("0111")
    # outputs 111