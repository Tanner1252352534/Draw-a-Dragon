import turtle  

t = turtle.Turtle()
t.speed(10)
t.color("red")

c_turtle = turtle.Turtle()
c_turtle.shape('triangle')
        
# turtle object
triangle_turtle = turtle.Turtle()
 
# the coordinates
# of each corner
shape =( (0,35), (0,0), (-18, 16) )

 
# registering the new shape
turtle.register_shape('triangle', shape)
 
# changing the shape to 'triangle'
triangle_turtle.shape('triangle')

triangle_turtle = turtle.Turtle()
 

shape =( (0,70), (0,35), (-18, 51) )

 

turtle.register_shape('triangle', shape)
 

triangle_turtle.shape('triangle')

triangle_turtle = turtle.Turtle()
 

shape =( (0,105), (0,70), (-18, 86) )


turtle.register_shape('triangle', shape)
 

triangle_turtle.shape('triangle')

triangle_turtle = turtle.Turtle()

shape =( (0,140), (0,105), (-18, 121) )


turtle.register_shape('triangle', shape)

triangle_turtle.shape('triangle')

triangle_turtle = turtle.Turtle()
 
shape =( (0,175), (0,140), (-18, 156) )


turtle.register_shape('triangle', shape)
 

triangle_turtle.shape('triangle')



#while True:
while True:
    
    #body/head
    t.forward(300)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(100)

#leg 1

    t.right(180)
    t.forward(100)
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(90)
    t.right(90)


#leg 2

    t.forward(25)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(90)
    t.right(90)

#leg 3

    t.forward(25)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(90)
    t.right(90)

#leg 4
    t.forward(25)
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(90)
    t.right(90)

#face/head stuff
    t.forward(50)
    t.left(90)
    t.forward(115)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(45)

#pupils starting bottom right of right eye
    t.left(90)
    t.forward(20)
    t.color("purple")
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.color("red")
    t.forward(35)
    t.left(90)
    t.forward(100)
    t.left(90)

#left pupil start
    t.forward(45)
    t.color("purple")
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.color("red")

#tail
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(30)

#wings
    t.left(270)
    t.forward(225)
    t.color("purple")
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(50)

#spikes
    t.right(135)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(23)
    t.left(45)
    t.forward(2)
    t.left(90)
    t.color("red")


