from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
from time import sleep

a = (0,110,90)
b = (0,0,0)
maze = [[a,a,a,a,a,a,b,a],
        [a,b,b,a,b,b,b,a],
        [a,b,a,a,b,a,a,a],
        [a,b,b,b,b,b,b,a],
        [a,b,a,a,a,a,b,a],
        [a,a,a,b,b,a,b,a],
        [a,b,b,b,b,b,b,a],
        [a,b,a,a,a,a,a,a]]

game_over = False

MC = (254,254,254)
x = 6
y = 0

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179:
            new_x -= 1
    if 181 < pitch < 359:
            new_x += 1

while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch,roll,x,y)
    maze[y][x] = MC
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
    
