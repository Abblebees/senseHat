from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
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
MC = (254,254,254)
x = 6
y = 0
maze[y][x] = MC

sense.set_pixels(sum(maze,[]))
