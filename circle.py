from turtle import *
from random import randrange
colors = ["red", "yellow", "cyan", "DarkOrange", "DeepPink", "DarkGreen", "chartreuse", "gold", "green", "pink", "OliveDrab", "orchid", "purple", "coral", "Tomato", "YellowGreen", "Indigo", "Brown", "MediumVioletRed", "Navy", "HotPink", "SkyBlue", "MidnightBlue", "DarkBlue", "DarkKhaki", "GreenYellow", "DarkSeaGreen", "Lavender", "RoyalBlue", "DarkViolet", "DarkRed"]
number = 0
degrees = 0
times = 0
while True:
    for i in range(4):
        forward(200)
        left(90)
    pencolor(colors[number])
    left(1)
    number = number + 1
    if number == 30:
        number = 0
    times = times+1
    print(times)
