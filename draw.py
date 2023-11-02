import turtle

def draw_vertical():    
    pen.up()
    pen.color("yellow")
    pen.width(10)
    pen.speed(10)
    pen.goto(-125, 300) 
    pen.pendown()
    pen.right(90)
    pen.forward(300*2)
    pen.color("yellow")
    pen.penup()
    pen.goto(125, 300) 
    pen.pendown()
    pen.forward(300*2)
    pen.penup()

    
def draw_horizontal():
    pen.color("red")
    pen.speed(15)
    pen.penup()
    pen.goto(-370, 100)
    pen.right(270) 
    pen.pendown()
    pen.forward(370*2)
    pen.penup()
    pen.goto(-370, -100) 
    pen.pendown()
    pen.forward(370*2)
    pen.penup()

def draw_x(x, y):
    pen.penup()
    pen.color("yellow")
    pen.speed(10)
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(45)
    pen.forward(70)
    pen.backward(140)
    pen.forward(70)
    pen.left(90)
    pen.forward(70)
    pen.backward(140)
    pen.forward(70)
    pen.penup()
    
def draw_o(x, y):
    pen.penup()
    pen.color("red")
    pen.speed(10)
    pen.goto(x, y)
    pen.pendown()
    pen.dot(70)
    pen.penup()
    
def turn(x,y):
    global turn_x
    global blocks_blocked
    global x_blocks
    global y_blocks
    global game_over_var
    
    if (x>=-370 and x<=-125 and y<300 and y>100):
        block = 1
        if  turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>=-125 and x<=125 and y<300 and y>100):
        block = 2
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif(x>125 and y<300 and y>100):
        block = 3
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>=-370 and x<=-125 and y<100 and y>-100):
        block = 4
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>=-125 and x<=125 and y<100 and y>-100):
        block = 5
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>125 and y<100 and y>-100):
        block = 6
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>=-370 and x<=-125 and y>-300 and y<-100):
        block = 7
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    elif (x>=-125 and x<=125 and y>-300 and y<-100):
        block = 8
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
    else:  
        block = 9
        if turn_x==True:
            x_blocks.append(block)
        else:
            y_blocks.append(block)
            
    if block not in blocks_blocked:
        blocks_blocked.append(block)
        draw(block,turn_x)
        if turn_x:
            turn_x = False  
        else:
            turn_x = True
    else:
        return
    if(turn_x==True):
        out = check_Win(y_blocks)
    else:
        out = check_Win(x_blocks)
    if out is not None:
        game_over(out[1])
    if len(blocks_blocked)==9:
        game_over_var = True
        game_end()

def game_over(x):
    l = block_coord(x[0])
    y = block_coord(x[2])
    pen.penup()
    pen.color("orange")
    pen.goto(l) 
    pen.pendown()
    pen.goto(y)
    pen.penup()         
    game_end()

def game_end():
    pen.color("yellow")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.speed(5)
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    pen.left(45)
    pen.forward(350)
    pen.left(90)
    pen.forward(320)
    pen.left(90)
    pen.forward(350*2)
    pen.left(90)
    pen.forward(320*2)
    pen.left(90)
    pen.forward(350*2)
    pen.left(90)
    pen.forward(320)
    pen.end_fill()
    pen.reset()
    screen.clearscreen
    pen.penup()
    pen.color("blue")
    pen.goto(0, 0)
    pen.pendown()
    pen.write("Click anywhere to play again, close the app to exit", align="center", font=("Arial", 16, "normal"))
    screen.onclick(game)    
    
def check_Win(blocks):
    for x in vertical:
        count = 0
        for y in blocks:
            for i in range(0,3):
                if y == x[i]:
                    count+=1
        if(count==3):
            return (True,x)
    for x in horizontal:
        count = 0
        for y in blocks:
            for i in range(0,3):
                if y == x[i]:
                    count+=1
        if(count==3):
            return (True,x)
    for x in diagonal:
        count = 0
        for y in blocks:
            for i in range(0,3):
                if y == x[i]:
                    count+=1
        if(count==3):
            return (True,x)
    
def block_coord(x):
    if(x==1):
        return(-245,200)
    if(x==2):
        return(0,200)
    if(x==3):
        return(245,200)
    if(x==4):
        return(-245,0)
    if(x==5):
        return(0,0)
    if(x==6):
        return(245,0)
    if(x==7):
        return(-245,-200)
    if(x==8):
        return (0,-200)
    if(x==9):
        return(245,-200)
    
    
def draw(block,turn_x):
    x= block_coord(block)
    if(turn_x==True):
        draw_x(x[0],x[1])
        turn_x=False
    else:
        draw_o(x[0],x[1])
        
def reset():
    global turn_x
    global blocks_blocked
    global x_blocks
    global y_blocks
    global game_over_var
    turn_x = True
    blocks_blocked=[]
    x_blocks=[]
    y_blocks=[]
    screen.clear()
    game_over_var = False   

def game(x,y):
    reset()
    pen.reset()
    draw_vertical()
    draw_horizontal()
    screen.onclick(turn)
    turtle.done()
    
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.bgcolor("blue")
turn_x = True
blocks_blocked=[]
x_blocks=[]
y_blocks=[]
game_over_var = False

vertical = [[1,4,7],[2,5,8],[3,6,9]]
horizontal=[[1,2,3],[4,5,6],[7,8,9]]
diagonal = [[1,5,9],[3,5,7]]

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(25)
pen.color("red")
pen.width(10)
game(0,0)