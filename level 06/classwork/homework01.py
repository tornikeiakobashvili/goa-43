from turtle import *

width(7)
color("brown")

speed(100)

penup()
goto(-150,-150)
pendown()

begin_fill()

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

end_fill()

begin_fill()

forward(115)
color("yellow")
left(90)

forward(115)
right(90)

forward(90)
right(90)

forward(115)
right(90)

end_fill()

penup()
goto(150,30)
pendown()
begin_fill()
color("brown")

back(150)
left(90)

forward(180)
right(90)

forward(150)

end_fill()

penup()
goto(-150,30)
pendown()
begin_fill()
forward(150)
left(90)



forward(180)
left(90)

forward(150)

end_fill()

penup()
goto(10,150)
pendown()

color("black")

left(90)
forward(100)

right(90)
forward(70)

right(90)
forward(50)

right(90)
forward(70)

penup()
goto(-380,-150)
pendown()

color("green")
begin_fill()
left(90)
forward(120)

left(90)
forward(800)

left(90)
forward(120)

left(90)
forward(800)
end_fill()


exitonclick()