# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file
"""
from  math import *
from turtle import *
from math import *


def sommet(c,x,y):
    up()
    setpos(x,y)
    down()
    circle(15)
    up()
    setpos(x,y+5)
    write(c,False,align="center",font=("Ariel",10,"normal"))



def arcp(x,y,z,t,p):
    setheading(0)
    up()
    setpos(z,t+30)
    left(90)
    down()
    circle(sqrt((x-z)*(x-z)+(y-t)*(y-t))/2, 180)
    up()
    setpos((x+z)/2,y+sqrt((x-z)*(x-z)+(y-t)*(y-t))/2+40)
    write(p, False, align="center", font=("Ariel",10,"normal"))
    up()


def graph(M):
    for i in range (len(M)):
        sommet(i,i*100,50)
    for i in range (len(M)):
        for j in range (i):
            if(M[i][j]!=0):
                arcp(100*j,50,100*i,50,M[i][j])


"""
Matrice M :
|0  1  7|
|1  0  4|
|7  4  0|
"""

clearscreen()
graph([[0,1,7],[1,0,4],[7,4,0]])
exitonclick()

"""
sommet("oui",0,0)
sommet("non",100,0)
arcp(0,0,100,0,"eheh")
"""