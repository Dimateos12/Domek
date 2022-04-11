import time
from turtle import *

speed(0)

# trawa
bgcolor("green")

# niebo

penup()
goto(-800, 0)
pendown()
color("deepskyblue")
begin_fill()

for i in range(2):
    forward(8000)
    left(90)
    forward(500)
    left(90)
end_fill()

# słońce

penup()
goto(-300, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

# chmury
penup()
goto(200,200)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(220,240)
pendown()
begin_fill()
circle(25)
end_fill()


penup()
goto(230,215)
pendown()
begin_fill()
circle(25)
end_fill()


penup()
goto(180,225)
pendown()
begin_fill()
circle(25)
end_fill()

# domek
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "wheat")
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# komin
penup()
goto(20,130)
pendown()
color("firebrick", "brown")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# dach
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# okno 1

penup()
goto(0,0)
pendown()
color("black","white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Linia na oknie

penup()
goto(0, 25)
color("black")
forward(50)

penup()
goto(25,0)
left(90)
forward(50)


# Okno 2

penup()
goto(-80,0 )
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# linie w oknie 2
penup()
goto(-80, 25)
color("black")
forward(50)

penup()
goto(-55,0)
left(90)
forward(50)

# Drzwi
penup()
goto(-40,-97)
right(90)
color("red")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# klamka

penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

# droga

penup()
goto(-100,-338)
pendown()
color("saddle brown")
begin_fill()
for i in range(2):
    forward(170)
    left(90)
    forward(235)
    left(90)
end_fill()

time.sleep(3)


