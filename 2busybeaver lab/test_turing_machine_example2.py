from turing_machine import TuringMachine
from test_turing_machine_example1 import print_states

transitions = {
        ('q0', '#'): ('End', '#', 'R'),
        ('End', ''): ('qa', '', 'R'),

        ('q0', '0'): ('FindDelimiter0', 'X', 'R'),
        ('FindDelimiter0', '#'): ('Check0', '#', 'R'),
        ('Check0', '0'): ('FindLeftmost', 'X', 'L'),

        ('q0', '1'): ('FindDelimiter1', 'X', 'R'),
        ('FindDelimiter1', '#'): ('Check1', '#', 'R'),
        ('Check1', '1'): ('FindLeftmost', 'X', 'L'),

        ('FindLeftmost', '0'): ('FindLeftmost', '0', 'L'),
        ('FindLeftmost', '1'): ('FindLeftmost', '1', 'L'),
        ('FindLeftmost', 'X'): ('FindLeftmost', 'X', 'L'),
        ('FindLeftmost', '#'): ('FindLeftmost', '#', 'L'),
        ('FindLeftmost', ''): ('FindNext', '', 'R'),

        ('FindNext', 'X'): ('FindNext', 'X', 'R'),
        ('FindNext', '0'): ('FindDelimiter0', 'X', 'R'),
        ('FindNext', '1'): ('FindDelimiter1', 'X', 'R'),
        ('FindNext', '#'): ('End', '#', 'R'),

        ('FindDelimiter0', '0'): ('FindDelimiter0', '0', 'R'),
        ('FindDelimiter0', '1'): ('FindDelimiter0', '1', 'R'),
        ('FindDelimiter1', '0'): ('FindDelimiter1', '0', 'R'),
        ('FindDelimiter1', '1'): ('FindDelimiter1', '1', 'R'),

        ('Check0', 'X'): ('Check0', 'X', 'R'),
        ('Check1', 'X'): ('Check1', 'X', 'R'),

        ('End', 'X'): ('End', 'X', 'R')
}
# # This machine matches identical strings of characters at either end of the delimiter, and transforms them into Xs
# # computation:
# #   - run ('q0', '#'), ('q0', '0'), ('q0', '1') respectively, base on the input first char (# , 0, or 1)
# #   - if 0, go state FindDelimiter0, or 1, go state FindDelimiter1
# #   - until # occur, we go state Check0 if was FindDelimiter0, or Check1 if was FindDelimiter1
# #   - if ('Check0', '0') or ('Check1', '1'), we go state FindLeftmost until ('FindLeftmost', '')
# #   - we then go state FindNext until a 0 or 1 find,
# #   - then go state FindDelimiter0 or FindDelimiter1 respectively based on input
# #   - repeat the process until ('FindNext', '#'), we go state End
# #   - if reach ('End', ''), we accpet the input

if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)
    def run(input_):
        w = input_
        print("Input:", w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w)
        print()

    # ACCEPTS
    run("#")

    # REJECTS - the first character is a 0
    # and the character at the end of the 1s is a 1
    run("0000#XXXX1")

    # REJECTS - it doesn't what character you have after tht first character
    # This flips the machine into  FindDelimiter0 and Check0 chain
    run("0111#XXXX1")

    # REJECTS - it doesn't what character you have after tht first character
    # This flips the machine into  FindDelimiter0 and Check0 chain
    run("0111#XXXX0")

    # REJECTS - this one reaches the end and checks the '0', and then
    # move back all the way to beginning
    run("0111#XXXX0")

    # ACCEPTS
    run("0#XXXX0")

    # ACCEPTS
    run("1#XXXX1")

    # REJECTS - only one 1 after #
    run("11#XXXX1")

    # ACCEPTS
    run("11#XXXX11")

    # ACCEPTS
    run("01#XXXX01")

    # ACCEPTS
    run("01#01")
    # tape output at the end: XX#XX

    # ACCEPTS
    run("101#101")
    # tape output at the end: XXX#XXX