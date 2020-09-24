import turtle

turtle.down()

def draw_petal():
    """This is the function that draws the petal of the flower"""

    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    """This is a function that draws the flower"""

    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_advanced():
    """This is the function that draws the flower
    and move the turtle`s head to the position for
    drawing the next flower"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    """This is the function that draws the bed of flowers (three flowers)"""

    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()
    turtle.done()

#draw_petal()
#draw_flower()
#draw_flower_advanced()
draw_flower_bed()