#A simple maze game on python by @Nips


import turtle
import math

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
        self.gold = 0

    def go_up(self):
        #calculate position to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #calculate spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_left(self):
        #calculate spot t move to
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_right(self):
        #calculate spot to move to
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) +(b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


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
"XX   TXXXXX             X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX,"
]

#adding treasure list
treasures = []

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
                #Adding cordinates to wall listen
                walls.append((screen_x, screen_y))

            #check if it is a P (represnting player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #check if it is a T
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

#Create class instances
pen = Pen()
player = Player()

#Creating walls
walls = []


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
    #check for player collission with treasure
    #iterate through player list
    for treasure in treasures:
        if player.is_collision(treasure):
            #add the treasure gold to the player gold
            player.gold += treasure.gold
            print("Player gold: {}".format(player.gold))
            #destroy te treasure
            treasure.destroy()
            #Remove treasurefrom treasures list
            treasures.remove(treasure)
    #Update screen
    wn.update()
