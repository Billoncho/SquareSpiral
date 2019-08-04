# SquireSpiral1.py
# Billy Ridgeway
# Creates a square spiral.

import turtle           # Imports the turtle library.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the pen's speed to fast.

# Creates a for loop to draw our square spiral.
for x in range (200):   # Set the range of the variable to 200.
    t.forward(2*x)      # Moves the pen forward 2 times the value of x.
    t.left(90)          # Turns the pen 90 degrees left.
