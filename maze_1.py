#A simple maze game on python by @Nips
#1% more

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game by @Nips")
wn.setup(700,700)

#Creating Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 24)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 24)

    def go_left(self):
        self.goto(self.xcor() -24, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 24, self.ycor())

#Creating list of levels
levels = [""]

#First levels
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX    P     XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX,"
]

#Add maze to mazes list
levels.append(level_1)

#Create Level SetUp Function
def setup_maze(level):
    for y in range (len(level)):
        for x in range (len(level[y])):
            #Get character at each x,y coordinates
            #NOTE order of x and y in the next line
            character = level[y][x]
            #Calculate screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
            
            #check if it is a P (represnting player)
            if character == "P":
                player.goto(screen_x, screen_y)

#Create class instances
pen = Pen()
player = Player()

#Set up the level
setup_maze(levels[1])

#Keyboard bindings
turtle.listen()
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")

#Turn off screen updates
wn.tracer(0)

#main game loop
while True:
    #Update screen
    wn.update()
