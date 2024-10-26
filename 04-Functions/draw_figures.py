import turtle
from figures import draw_square 

window = turtle.Screen()
window.bgcolor("lightgreen")

side_length = 100
draw_square(side_length)

window.mainloop()
