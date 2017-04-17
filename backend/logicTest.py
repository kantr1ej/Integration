#                  Main integration program for                      #
#               Agri-Starts Senior Design Project                    #
#              UCF Senior Design Project - Blue Agave                #
#        Application written by Erik Kantrowitz for Agri-Starts      #

# Control GPIO pins
#   M1 | S0 | S1 | S2 | S3 | S4 |
# | 12 | 07 | 11 | 13 | 15 | 16 |  Board Val
# | 18 | 04 | 17 | 27 | 22 | 23 |  BCM Val

# filling GPIO pins
# | W0 | W1 | W2 | W3 | W4 |
# | 22 | 29 | 31 | 36 | 37 |  Board Val
# | 25 | 05 | 06 | 16 | 26 |  BCM Val

# possible LED indicator
# | L0 |
# | 18 |
# | 24 |

import signal
import sys
import RPi.GPIO as gpio
import math
from back import Back
from time import sleep

back = Back()



def switchEnd():
    # back.ledBlink
    back.motorOff
    print "TRIGGER WARNING:  End switch triggered"

def run_program():
    while 1:
        if gpio.input(4):
            # switchFill()
            print "TRIGGER WARNING:  Filling switch triggered"
            sleep(2.65)
            back.motorOff()
            sleep(4)

        # if swc[1] == 0:
        #     ## logic for dealing with a block in the line
        #     ## would go here
        #     # switchBlock()
        #
        # if swc[2] == 0:
        #     #capping
        #     capped += 1
        #
        # if swc[3] == 0:
        #     ## logic for dealing with a block in the line
        #     ## would go here
        #     # switchBlock()
        #
        # if swc[4] == 0:
        #     switchEnd()
        #     complete += 1

        else:
            back.motorOn()
            print "running"
            sleep(0.1)

        # return (filled, capped, complete)

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n) ").lower().startswith('y'):
            back.motorOff()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        back.motorOff()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
