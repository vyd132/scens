import random

color=[255,0,0]
number=0
display='first'

def color_change():
    global color
    color=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]