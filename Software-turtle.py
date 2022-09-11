#this is the welcoming program.
def welcome():
    print ("Hello! Welcome to dragans assesment!")
    #takes you to the menu program.
    menu()
    
#the menu sub-program so the user can choose what the turtle displays.
def menu():
    #different runnable sub-programs.
    print("~PROGRAM OPTIONS~")
    print("~TURTLE SHAPES~")
    print("1.square")
    print("2.circle")
    print("3.polygon")
    print("4.squareInsideASquare")
    print("5.polygonInsideAPolygon")
    print("6.changePensize")
    print("7.grid")
    print("8.polygonRow")
    print("9.tree")
    print("10.forest")
    print("~TURTLE GRAPHS~")
    print("a.BarGraph(small numbers)")
    print("b.BarGraph(large numbers)")
    print("c.mathTest")
    print("d.lineGraph")
    print("e.quadraticEquation")
    #askes witch program you want to run.
    program=input("Which program would you like to run?")
    #figures out what program you want to run and starts the sub-program
    if program=='1':
        square()
    elif program=='2':
        circle()
    elif program=='3':
        polygon()
    elif program=='4':
        squareInSquare()
    elif program=='5':
        polygonInPolygon()
    elif program=='6':
        setPenSize()
    elif program=='7':
        grid()
    elif program=='8':
        polygonRow()
    elif program=='9':
        tree()
    elif program=='10':
        forest()
    elif program=='a':
        stringOfValues()
    elif program=='b':
        stringOfLargeValues()
    elif program=='c':
        mathTest()
    elif program=='d':
        lineGraph()
    elif program=='e':
        quadraticEquation()
    else:
        #if the user inputs an invalid awnser it will display "try again".
        print("ops! that wasnt the correct value! try agian")
        #calls back its self untill the user inputs a valid awnser.
        menu()

    #reapeat sub program used at the end of all my other user callable programs to see if they want to continue using the program.
def reapeat():
    #asks user if they want to create another shape or if they want to quit the program.
    agian=input("do you want to make another shape? y/n")
    #if the awnser is "y" it will call back to welcome.
    if agian=='y':
        turtle.clear()
        welcome()
    #if the awnser is "n" it will quit the program
    elif agian=='n':
        exit()
    #setPenSize is a user callable sub program so the they can change the size of the pen tip.
def setPenSize():
    #asks what size the pen should be.
    penSize=int(input("How big would you like the pen to be?"))
    #changes pen size to the request.
    turtle.pensize(penSize)
    #calls back to reapeat to see if they want to continue with the program.
    reapeat()
    #square is a user callable sub-program that creates a customizible cubiod.
def square():
    #asks user how big the square should be.
    sideLength=int(input("How big woud you like the square?"))
    #a loop that will repeat four times.
    for i in range (4):
        #turtle moves forward by the desired amount asked above then turns ninty degrees to the left.
        turtle.forward(sideLength)
        turtle.left(90)
        #calls the reapeat sub-program.
    reapeat()

    #circle is a user callable sub-program used to create a circle.
def circle():
    #asks user how large they would like the circle to be.
    r=int(input("how big would you like your circle?"))
    #a loop that will repeat for 360 times to create the diamiter of the circle.
    for i in range (0,360):
        #turtle moves forward by the desired amount.
        turtle.forward(r)
        #turtle turns left by the desired amount devided by four.
        turtle.left(r/4)
        #calls the reapeat sub-program.
    reapeat()

    #polygon is a user callable sub-program used to create a polygon.
def polygon():
    #asks user for the number of sides.
    sides=int(input("how many sides would you like for your polygon?"))
    #asks user for the length of each side.
    sideLength=int(input("how long would you like the sides of your polygon?"))
    #a loop that will repeat for x where x is the number of imputed sides.
    for i in range(sides):
        #turtle moves forward by requested sidelength.
        turtle.forward(sideLength)
        #turtle turns right by 360 divided by the requested number of sides.
        turtle.right(360/sides)
        #calls the reapeat sub-program.
    reapeat()

    #squareInSquare a user callable sub-program used to create consentric squares.
def squareInSquare():
    #asks user for length of sides and the number of squares.
    sides=int(input("how long do you want the side to be?"))
    squares=int(input("how many squares?"))
    #sets varibles "x" and "y" to zero.
    x=0
    y=0
    #a loop that will reapeat for the requested number of squares.
    for i in range(squares):
        #calls the drawSquare subprogram.
        drawSquare(sides,x,y)
        #reduces the value of the side length by ten.
        sides=sides-10
        #increses the value of x by 5
        x=x+5
        #reduces the value of y by 5
        y=y-5
    #calls the reapeat sub-program.
    reapeat()
    #a sub-program called by squareInSquare to create a square.
def drawSquare(sides,x,y):
    #lifts the pen up so it wont create lines.
    turtle.penup()
    #sets the turtles position to the x variable.
    turtle.setx(x)
    #sets the turtles position to the y variable.
    turtle.sety(y)
    #put the pen down so it will create lines
    turtle.pendown()
    #a loop that will repeat four times to create a square.
    for i in range(4):
        #moves the turtle forward by the requested length of sides.
        turtle.forward(sides)
        #turns the turtle right by ninty degrees.
        turtle.right(90)

    #a user callable sub-program to create consentric polygons.
def polygonInPolygon():
    #asks user for the number of sides, side length and the number of polygons.
    sides=int(input("how many sides on the polygon?"))
    sideLength=int(input("how long do you want the sides to be?"))
    numberOfPolygons=int(input("how many polygons?"))
    #sets turtle location to "0,0"
    turtle.goto(0,0)
    #sets turtle pointing to the right of the screen.
    turtle.setheading(0)
    #a loop that repeats for the requested number of polygons.
    for i in range(numberOfPolygons):
        #calling the drawpolygon sub-program.
        drawPolygon(sides,sideLength)
        #changes sideLength variable by -10
        sideLength=sideLength-10
        turtle.right((180-360/sides)/2)
        turtle.penup()
        #moves turtle forward by 10.
        turtle.forward(10)
        turtle.pendown()
        #turns turtle tight by 180 minus 360 divided by pi.
        turtle.left((180-360/sides)/2)
    reapeat()
        
    #a sub-program called by polygonInPolygon used to create a polygon
def drawPolygon(sides,radius):
    turtle.pendown()
    #an equastion to calculate the distance need to move towards the centre of the polygon.
    sideLength=2*radius*math.sin(math.pi/sides)
    #a loop used to create a polygon based on the number of sides and their length.
    for i in range(sides):
        turtle.forward(sideLength)
        turtle.right(360/sides)
   
#a user callable sub-program used to create a grid pattern across the screen with changable distances between them.
def grid():
    #asks user for both the "x" and "y" variable.
    y=int(input("what would you like the y distance to be?"))
    x=int(input("what would you like the x distance to be?"))
    #creates variables for the hight and width of the screen.
    windowWidth=turtle.window_width()
    windowHeight=turtle.window_height()
    turtle.penup()
    #moves the turtle to the top right corner of the screen.
    turtle.goto(0,0)
    turtle.forward(windowWidth/2)
    turtle.left(90)
    turtle.forward(windowHeight/2)
    turtle.right(90)
    turtle.pendown()
    #a loop used to create the grid lines along the x axis.
    for i in range(int(windowWidth)):
        turtle.backward(windowWidth)
        turtle.right(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(windowWidth)
    #moves the turtle to the top right corner of the screen.
    turtle.penup()
    turtle.goto(0,0)
    turtle.forward(windowWidth/2)
    turtle.left(90)
    turtle.forward(windowHeight/2)
    turtle.pendown()
    turtle.right(180)
    #a loop used to create the grid lines along the y axis.
    for j in range(int(windowHeight)):
        turtle.forward(windowHeight)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(windowHeight)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(90)
        #calls the reapeat sub-program.
    reapeat()

#a user callable sub-program used to created rows of polygons.
def polygonRow():
    #defines the windows height and width.
    windowWidth=turtle.window_width()
    windowHeight=turtle.window_height()
    turtle.penup()
    #asks user for the number of sides, their length, the number of rows and the number of columns.
    sides=int(input("how many sides on your polygons would you like?"))
    sideLength=int(input("how long do you want the sides of your polygons?"))
    columnNumber=int(input("how many columns of polygons would you like?"))
    rowNumber=int(input("how many rows of polygons would you like?"))
    #defines x and yPos to half the windo height and width
    xPos=windowWidth/2
    yPos=windowHeight/2
    #using the set x and yPos it travel to those cords.
    turtle.goto(xPos,yPos)
    turtle.pendown()
    #sets the current position as a variable
    currentPos=turtle.position()
    #a loop the will create the desired number of rows and columns.
    for j in range (columnNumber):
        for i in range (rowNumber):
            #calls on the drawRowPolygon sub-program to create a polygon.
            drawRowPolygon(sides,sideLength,xPos,yPos)
            xPos=xPos+(sideLength*2)
            #gets ready to draw another polygon by returning to original position then moving and setting that to current pos.
        turtle.penup()
        turtle.goto(currentPos)
        turtle.right(90)
        turtle.forward(sideLength*(sides/2))
        turtle.left(90)
        currentPos=turtle.position()
        turtle.pendown()
        #calls the reapeat sub-program.
    reapeat()
    #a sub-program called on by polygonRow used to create the polygons.
def drawRowPolygon(sides,sideLength,xPos,yPos):
    turtle.penup()
    turtle.backward(sideLength*(sides/3))
    turtle.pendown()
    #a loop that will repeat equal to the number of inputed sides to create a polygon.
    for i in range(sides): 
        turtle.forward(sideLength) 
        turtle.right(360/sides) 
    #a user callable sub-program to create a randomly generated tree.
def tree():
    turtle.penup()
    #sets variables for the width and height of the screen.
    windowWidth=int(turtle.window_width())
    windowHeight=int(turtle.window_height())
    #sets variables for the trees position and size of canopy randomly.
    turtleCurrentX=random.randint(-windowWidth/2,windowWidth/2)
    turtleCurrentY=int(random.randint(1,60))
    turtleCurrentY=turtleCurrentY-turtleCurrentY*2
    polygonSides=random.randint(5,9)
    polygonSideLength=random.randint(40,60)
    #an array to store different colors for the log.
    myBrownList = ["peru", "goldenrod", "dark goldenrod"]
    #uses the array above to randomly chose an option from among them and use it as the log color. 
    trunkColor=random.choice(myBrownList)
    #picks a random size and length for the log.
    PenSize=random.randint(8,15)
    logLength=random.randint(100,300)
    #using the random varibales at the start it  goes to a random position and sets pen color and size to the previously determind random amount.
    turtle.goto(turtleCurrentX,turtleCurrentY)
    turtle.setheading(90)
    turtle.pencolor(trunkColor)
    turtle.pensize(PenSize)
    turtle.pendown()
    #runs the branch sub-program to create branches for the tree.
    branch(turtleCurrentY,turtleCurrentX,logLength,trunkColor,PenSize)
    turtle.penup()
    turtle.pencolor(trunkColor)
    turtle.pensize(PenSize)
    #goes back to originally chosen random location then creates the log.
    turtle.goto(turtleCurrentX,turtleCurrentY)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(logLength)
    #calls the treetp sub-program to create the canopy for the top of the tree.
    treetop(turtleCurrentY,turtleCurrentX,polygonSides,polygonSideLength,1)
    
    #the treetop sub program is called by the tree and branch sub-programs and is used to create randomly generated polygons as canopys.
def treetop(turtleCurrentY,turtleCurrentX,polygonSides,polygonSideLength,numberOfPolygons):
    #creates an array to store color values for the polygons
    leafSpecs()
    myGreenList = ["sea green", "forest green", "dark green"]
    turtleDirection=int(turtle.heading())
    #checks witch direction the turtle is pointing through an if loop.
    if turtleDirection < 80:
        turtle.setheading(90)
        turtle.backward(polygonSideLength/2)
        #random picks a color for the polygons from the color list.
        turtle.fillcolor(random.choice(myGreenList))
        #tells the turtle that we want the next shape to be filled
        turtle.begin_fill()
        # a loop to create the randomly generated polygons.
        for i in range(polygonSides): 
            turtle.forward(polygonSideLength) 
            turtle.right(360/polygonSides)
        #ends the fill making them a solid color.
        turtle.end_fill()
        turtle.penup()
        #sets turtle back up.
        turtle.right((180-360/polygonSides)/2)
        turtle.forward(polygonSides/math.pi)
        turtle.left((180-360/polygonSides)/2)
        polygonSideLength=polygonSideLength-(polygonSides/math.pi)
        turtle.pendown()
        # deos the same loop except checking for differnt directions
    elif turtleDirection > 100:
        turtle.setheading(90)
        turtle.backward(polygonSideLength/2)
        turtle.fillcolor(random.choice(myGreenList)) 
        turtle.begin_fill()
        for i in range(polygonSides): 
            turtle.forward(polygonSideLength) 
            turtle.left(360/polygonSides)
        turtle.end_fill()
        turtle.penup()
        turtle.left((180-360/polygonSides)/2)
        turtle.forward(polygonSides/math.pi)
        turtle.right((180-360/polygonSides)/2)
        polygonSideLength=polygonSideLength-(polygonSides/math.pi)
        turtle.pendown()
        # deos the same loop except checking for differnt directions
    elif turtleDirection==90:
        turtle.right(90)
        turtle.backward(polygonSideLength/2)
        turtle.fillcolor(random.choice(myGreenList)) 
        turtle.begin_fill()
        for i in range(polygonSides): 
            turtle.forward(polygonSideLength) 
            turtle.left(360/polygonSides)
        turtle.end_fill()
        turtle.penup()
        turtle.left((180-360/polygonSides)/2)
        turtle.forward(polygonSides/math.pi)
        turtle.right((180-360/polygonSides)/2)
        polygonSideLength=polygonSideLength-(polygonSides/math.pi)
        turtle.pendown()
    # branch is a sub-program called by the tree sub-program to create branches.
def branch(turtleCurrentY,turtleCurrentX,logLength,trunkColor,PenSize):
    #randomly selects values for the amount of sides, pencolor, pensize and sidelength.
    polygonSides=random.randint(5,9)
    turtle.pencolor(trunkColor)
    turtle.pensize(PenSize)
    polygonSideLength=random.randint(15,30)
    #a loop to create branchs of random length at random points on the tree
    for i in range (random.randint(0,6)):
        turtle.penup()
        turtle.goto(turtleCurrentX,turtleCurrentY)
        turtle.setheading(90)
        turtle.pendown()
        turtle.pencolor(trunkColor)
        turtle.pensize(PenSize)
        turtle.forward(random.randint(25,logLength))
        turtle.setheading(random.choice([45,60,30,135,150,120]))
        turtle.forward(random.randint(10,75))
        #calls the sub-program treetop to create a polygon
        treetop(turtleCurrentY,turtleCurrentX,polygonSides,polygonSideLength,polygonSides)
        
#a sub-program called by treetop to set pensize and color for the outline of the canopy
def leafSpecs():
    turtle.pencolor("green")
    turtle.pensize(5)
#a sub-program used to create the backround for the forest sub-program
def ground():
    #sets the backround color to a shade of blue.
    turtle.bgcolor("dodger blue")
    windowWidth=int(turtle.window_width())
    windowHeight=int(turtle.window_height())
    turtle.pencolor("forest green")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0,0)
    turtle.backward(windowWidth/2)
    turtle.pendown()
    #i asign three variables differing values, these will be used to create a gradient.
    i=0
    r = 17
    g = 199
    b = 65
    turtle.colormode(255)
    turtle.color(0,0,255)
    #a for loop to create the grass gradient, after every loop it changes the value of three variables that change the color.
    for i in range(7):
        turtle.pencolor((r, g, b))
        r = int(r-0.25)
        g = int(g-5)
        b = int(b-2.5)
        turtle.setheading(270)
        turtle.forward(10)
        turtle.setheading(0)
        turtle.forward(windowWidth)
        turtle.backward(windowWidth)
    #reset the three variable to new values to create another gradient.
    i=0
    r = 195
    g = 111
    b = 15
    turtle.colormode(255)
    turtle.color(0,0,255)
    for i in range(33):
        turtle.pencolor((r, g, b))
        r = int(r-5)
        g = int(g-2.5)
        b = int(b-0.25)
        turtle.setheading(270)
        turtle.forward(10)
        turtle.setheading(0)
        turtle.forward(windowWidth)
        turtle.backward(windowWidth)
    
   #a user callable sub-program used to create a forest .                    
def forest():
    windowWidth=turtle.window_width()
    windowHeight=turtle.window_height()
    #asks user for the number of trees they want.
    treeNumber=int(input("how many trees would you like?"))
    #calls on the ground sub-program
    ground()
    turtle.penup()
    turtle.goto(random.randint(-windowWidth/2,windowWidth/2),windowWidth/4)
    turtle.pendown()
    turtle.pencolor("gold")
    turtle.pensize(150)
    turtle.forward(1)
    #a for loop that will repeat for the number of requestes trees running the tree sub-program each time.
    for i in range(treeNumber):
        tree()
    #calls the reapeat sub-program.
    reapeat()

#a sub-program called by graph based subprograms, it is used to create the x and y planes for the graph.
def linesOfAGraph():
    turtle.penup()
    turtle.goto(-300,-300)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(600)
    turtle.goto(-300,-300)
    turtle.setheading(90)
    turtle.forward(600)
    turtle.goto(-300,-300)

#a user callable sub-program to create a bargraph of a string of values
def stringOfValues():
    numbers=input("enter string of numbers e.g. 12345")
    arrayValue=0
    linesOfAGraph()
    #a for loop that will repeat for the length of inputed numbers.
    for i in range(len(numbers)):
        #changes the hieght of each bar based on the number and the amount of number inputed.
        graphValue=(int(numbers[arrayValue]))
        graphHieght=graphValue/9*600
        graphWidth=600/len(numbers)
        turtle.setheading(90)
        turtle.forward(graphHieght)
        turtle.right(90)
        turtle.forward(graphWidth)
        turtle.right(90)
        turtle.forward(graphHieght)
        arrayValue=arrayValue+1
        #calls the reapeat sub-program.
    reapeat()
    #a user callable sub-program to create a bargraph of a string of multiple large values
def stringOfLargeValues():
    numbers=input("enter string of numbers e.g. 1,2,3,4")
    numbers=numbers.split(",");
    arrayValue=0
    linesOfAGraph()
    #a for loop that will repeat for the length of inputed numbers.
    for i in range(len(numbers)):
        #changes the hieght of each bar based on the number and the amount of number inputed.
        graphValue=(int(numbers[arrayValue]))
        graphHieght=graphValue/99*600
        graphWidth=600/len(numbers)
        turtle.setheading(90)
        turtle.forward(graphHieght)
        turtle.right(90)
        turtle.forward(graphWidth)
        turtle.right(90)
        turtle.forward(graphHieght)
        arrayValue=arrayValue+1
        #calls the reapeat sub-program.
    reapeat()
    #a sub-program used to calculate the sum of a string of numbers.
def addition(array):
    Sum=0
    for i in range(len(array)):
        Sum=Sum+int(array[i])
    return Sum
    #a sub-program used to calculate the biggest number in a string of numbers
def maximum(array):
    Max=0
    for i in range(len(array)):
        if int(array[i])>Max:
            Max=int(array[i])
    return Max
    #a sub-program used to calculate the smallest number in a string of numbers
def minimum(array):
    Min=99999999
    for i in range(len(array)):
        if int(array[i])<Min:
            Min=int(array[i])
    return Min
    #a sub-program used to calculate the average out of a string of numbers
def average(array):
    avg=addition(array)/int(len(array))
    return avg
    #a sub-program used to calculate the standard deviation of a string of numbers
def standardDeviation(array):
    for i in range(len(array)):
        STDV=int(array[i])-average(array)
        STDV=STDV*STDV
        STDV/int(len(array))
        math.sqrt(STDV)
    return STDV


#a user callable sub-program that calls on all the other math based sub-programs and prints their awnsers based on an inputed string of numbers
def mathTest():
    mathArray=input("enter a string of characters e.g. 112345754")
    addition(mathArray)
    print("summary",addition(mathArray))
    maximum(mathArray)
    print("maximum",maximum(mathArray))
    minimum(mathArray)
    print("minimum",minimum(mathArray))
    average(mathArray)
    print("average",average(mathArray))
    standardDeviation(mathArray)
    print("standardDeviation",standardDeviation(mathArray))
    reapeat()

    #a user callable sub-program to show the size of numbers through a line graph
def lineGraph():
    numbers=input("enter string of numbers e.g. 1,2,3,4")
    numbers=numbers.split(",");
    arrayValue=0
    linesOfAGraph()
    x1=turtle.xcor()
    y1=turtle.ycor()
    #creates two arrays to store x and y coardinants.
    Yarray=[]
    Xarray=[]
    turtle.penup()
    for i in range(int(len(numbers))):
        graphValue=(int(numbers[arrayValue]))
        graphHieght=graphValue/99*600
        graphWidth=600/len(numbers)
        turtle.setheading(90)
        turtle.forward(graphHieght)
        #stores x and y cords and each point of the graph and stores them in an array.
        Yarray.append(turtle.ycor())
        Xarray.append(turtle.xcor())
        turtle.right(90)
        turtle.forward(graphWidth)
        turtle.right(90)
        turtle.forward(graphHieght)
        arrayValue=arrayValue+1
    turtle.pendown()
    turtle.goto(-300,-300)
    #uses the stored arrays and moves to them in the proper succcsession.
    for j in range(int(len(Xarray))):
        turtle.goto(Xarray[j],Yarray[j])
        #calls the reapeat sub-program.
    reapeat()

    #this is a user callable sub-program that uses quadratic equations to create a parabola.
def quadraticEquation():
    #asks user for formula data.
    A=int(input('What do you want as the A value'))
    B=int(input('What do you want as the B value'))
    C=int(input('What do you want as the C value'))
    #creates the y and x planes.
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(600)
    turtle.backward(1200)
    turtle.goto(0,0)
    turtle.setheading(90)
    turtle.forward(600)
    turtle.backward(1200)
    turtle.goto(0,0)
    turtle.penup()
    #goes to the first point on the parabola.
    X=-100
    Y=((A*X**2)+(B*X)+C)
    turtle.goto(X,Y)
    turtle.pendown()
    #creates the parabola through reapeatingg the formula multiple times and going to the x and y coordinates.
    while X < 100:
        Y=((A*X**2)+(B*X)+C)
        turtle.goto(X,Y)
        X=X+1
    reapeat()

    
    
#the main program that imports the different outside variable to preform  designated tasks.
import turtle
import math
import random
#changes turtles speed and visibility also changes pensize and sets the color mode to 255.
turtle.hideturtle()
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(1)
#runs the welcome sub-program.
welcome()
