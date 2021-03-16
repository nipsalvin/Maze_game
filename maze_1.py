#A simple maze game on python by @Nips
#python 2 & python 3 cOMPATIBLE
#Enemies now with AI

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game by @Nips")
wn.setup(700,700)
wn.tracer(0)

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
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #calculate spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_left(self):
        #calculate spot t move to
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()

        #check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_right(self):
        #calculate spot to move to
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()

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
    
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        
        #Check if player is close
        #if so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
        
        #Calculate spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if space has walls
        if (move_to_x, move_to_y)not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose different direction
            self.direction = random.choice(["up", "down", "right", "left"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    #defining parameters of method "is_close"
    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False
    
    def destroy(self):
        self.goto(2000, 2000)
        self.hhideturtle()

#Creating list of levels
levels = [""]

#First levels
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  EXXXXXX    P     XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX EXXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX EX",
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
"XXXX  E                 X",
"XXXXXXXXXXXXXXXXXXXXXXXXX,"
]

#adding treasure list
treasures = []

#Adding enemy list
enemies = []

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

            #check if it is an E (representing enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

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

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

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
    
    #Iterate through enemy list to see if player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")
    
    #Update screen
    wn.update()
