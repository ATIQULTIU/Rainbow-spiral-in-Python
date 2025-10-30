import turtle
import math

# Create turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Define rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw spiral pattern
for i in range(360):
    t.pencolor(colors[i % 7])  # Cycle through colors
    t.forward(i * 0.5)         # Move forward increasing distance
    t.right(59)                # Turn right to create spiral

# Finish drawing
turtle.done()
