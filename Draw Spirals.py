import turtle
t=turtle.Pen()
spirals=input("Enter the number of spirals you want:")
spirals=int(spirals)
for i in range(0,spirals):
    t.forward(100)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.right(90)
    
    
