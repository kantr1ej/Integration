import sys
import signal
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

def run_program():

    print("       Switch Testing Program is running.          ")
    print(" ------------------------------------------------  ")
    print(" To check if a switch is working correctly please  ")
    print(" manually press the two switches in simultaneously ")
    print(" ------------------------------------------------  ")
    print("    To exit the program press control-c            ")

    while 1:
       print "switch 1 is reading as: ", gpio.input(4)
       sleep(2)
       print "switch 2 is reading as ", gpio.input(27)
       sleep(2)



def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n) ").lower().startswith('y'):
            gpio.cleanup()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        gpio.cleanup()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
