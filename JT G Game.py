from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
from time import sleep

s = (0,0,0)
T = (255,255,0)
r = (204,0,0)
g = (0,254,0)
a = (0,110,90)
b = (0,0,0)
maze = [[a,a,a,a,a,a,s,a],
        [a,b,T,a,b,b,s,a],
        [a,b,a,a,b,a,a,a],
        [a,b,b,b,b,b,b,a],
        [a,b,a,a,a,a,b,a],
        [a,a,a,b,b,a,r,a],
        [a,b,b,b,b,b,b,a],
        [a,g,a,a,a,a,a,a]]

maze_non = [[a,a,a,a,a,a,b,a],
            [a,b,T,a,b,b,b,a],
            [a,b,a,a,b,a,a,a],
            [a,b,b,b,b,b,b,a],
            [a,b,a,a,a,a,b,a],
            [a,a,a,b,b,a,b,a],
            [a,b,b,b,b,b,b,a],
            [a,g,a,a,a,a,a,a]]

game_over = False
w = (254,254,254)
x = 6
y = 0

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != a:
        return new_x, new_y
    elif maze[new_y][x] != a:
        return x, new_y
    elif maze[y][new_x] != a:
        return new_x, y
    else:
        return x,y

def check_gate(x,y,new_x,new_y):
    if maze[new_y][new_x] != r:
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    else:
        return x,y

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179 and x != 0:
            new_x -= 1
    elif 181 < pitch < 359 and x != 7:
            new_x += 1
    if 1 < roll < 179 and y != 7:
        new_y += 1
    elif 359 > roll > 179 and y != 0:
        new_y -= 1
    new_x, new_y = check_wall(x,y,new_x, new_y)
    new_x, new_y = check_gate(x,y,new_x, new_y)
    return new_x, new_y

most_recent_maze = maze

while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch,roll,x,y)
    if maze[y][x] == g:
        sense.show_message("YOU GOT THIS VICTORY ROYALE")
        game_over = True
    maze[y][x] = w
    if maze[y][x] == T:
        most_recent_maze = maze_non
        sense.set_pixels(sum(most_recent,[]))
    sense.set_pixels(sum(most_recent_maze,[]))
    sleep(0.05)
    maze[y][x] = b

