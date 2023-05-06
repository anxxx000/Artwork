#trial
def star(t,size,color):
    
    """ (Turtle, float, str) -> NoneType

    Draws a star with a given size and a given color
    
    """
    
    t.fillcolor(color) #fill the shape according to the color given to the parameter
    
    t.begin_fill() #start filling the color
    
    for i in range(5): #repeat 5 times to complete the shape 
        
        t.forward(size) #if size is bigger, the star will be bigger
        
        t.right(144) #turn to draw star's hands
        
        t.forward(size)
        
        t.left(72) #turn to prepare drawing the next hand
        
    t.end_fill() #stop filling the color 
    
    
    
def triangle(t):
    
    """ (Turtle) -> NoneType

    Draws a green triangle
    
    """
    
    t.fillcolor("green") #green color
    
    t.begin_fill() #start filling the color
    
    for i in range(3): #repeat 3 times to complete the shape
        
        t.forward(130) #side length of the triangle
        
        t.left(120) #turn to prepare drawing next side
        
    t.end_fill() #stop filling the color
    
    
    
def tree(t):
    
    """ (Turtle) -> NoneType

    Draws a tree with function of triangles that has been defined previously
    
    """
    
    for i in range(3): #repeat 3 times to draw triangles one on another
        
        triangle(t) #function of triangle previously defined
        
        t.left(90)
        
        t.penup() 
        
        t.forward(60) #to go higher for drawing the next one
        
        t.pendown() #pen down to prepare drawing the next triangle
        
        t.right(90) #turn to prepare drawing the next triangle
        
        
        
def tree_trunk(t):
    
    """ (Turtle) -> NoneType

    Draws a brown tree trunk
    
    """
    
    t.fillcolor("brown")
    
    t.begin_fill()
    
    for i in range(2): #repeat 2 times to draw the rectangle trunk
        
        t.forward(50) #trunk width
        
        t.right(90) #angle turn
        
        t.forward(120) #trunk height
        
        t.right(90) #angle turn
        
    t.end_fill()
    
    
    
def christmas_tree(t):
    
    """ (Turtle) -> NoneType

    Draws a christmas tree 
    
    """
    
    tree_trunk(t) #function of tree trunk
    
    t.left(180)
    
    t.penup()
    
    t.forward(40) #go to prepare drawing the tree body
    
    t.right(180) #turn to the best position to draw the tree body
    
    tree(t) #function of tree
    
    t.left(90)
    
    t.penup()
    
    t.forward(70)
    
    t.right(90) #turn to face the tip of the tree
    
    t.forward(74) #go to the tip of the tree
    
    t.pendown() #pendown to draw the star on top of the tree
    
    star(t,size=20,color="yellow") #function of star
    
    

def sign(t):
    
    """ (Turtle) -> NoneType

    Draws the letter A(first letter of my first name)
    
    """
    
    t.forward(40) #first stroke
    
    t.right(120) #turn to draw second stroke
    
    t.forward(40) #second stroke
    
    t.right(180) #turn to prepare to go to the middle
    
    t.forward(20) #go to the middle 
    
    t.left(60) #turn to prepare for drawing the third stroke
    
    t.forward(20) #third stroke 
    
    t.penup() #finished
    
    t.forward(100)



def import_turtle():
    
    """ () -> Turtle

    Returns turtle that is going to be used in the my_artwork() function
    
    """
    
    import turtle #import the module
    
    t=turtle.Turtle() #define t to be the turtle
    
    #t.speed("fastest") #speed up t
    
    return t
 
 

def my_artwork():
    
    """ () -> NoneType

    Draws the chistmas tree followed by the signature
    
    """
    
    t = import_turtle() #import_turtle() function
    
    christmas_tree(t) #christmas_tree(t) function
    
    t.penup()
    
    t.forward(50) #go to another empty space for signature
    
    t.pendown() #pen down to prepare to sign
    
    t.left(60) #turn to the best position to sign
    
    sign(t) #sign(t) function


