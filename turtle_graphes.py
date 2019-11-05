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



def arc(x,y,z,t,p):
    if (p == 0):
        setheading(0)
        up()
        setpos(z,t+30)
        left(90)
        down()
        circle(sqrt((x-z)*(x-z)+(y-t)*(y-t))/2, 180)
    else:
        setheading(0)
        up()
        setpos(z, t + 30)
        left(-90)
        down()
        circle(sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2, 180)



def arcp(x,y,z,t,p):
    if (x < z):
        p = 0
        arc(x,y,z,t,p)
        up()
        setpos(x + sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2, y + sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2)
    else:
        p = 1
        arc(x, y, z, t, p)
        up()
        setpos(z + sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2, y - sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2)
    up()
    down()
    write(p, False, align="center", font=("Ariel",10,"normal"))
    up()
    setpos(0,0)


def matprod(a,b):
    n = len(a)
    c = zero((n,n))
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                if (s != 1):
                    s = a[i][k] * b[k][j]
            c[i][j] = s
    return c


def chemin(M):
    n = len(M)
    A = zero((n,n))
    B = zero((n,n))
    p = log(n,2)
    A = M
    for i in range(p):
        B = matprod(A,A)
        A = B
    return A


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
M = [[0,1,7],[1,0,4],[7,4,0]]
chemin(M)
exitonclick()

"""
sommet("oui",0,0)
sommet("non",100,0)
arcp(0,0,100,0,"eheh")
"""