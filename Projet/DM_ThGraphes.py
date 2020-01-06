# -*- coding: utf-8 -*-
"""
@authors: Estelle Fiket & Inès Thao


But : 
    Vecteur tp : planning au plus vite
    Vecteur ts : Planning séqueniel
    Indication au cas où le graphe est cyclique
"""


import numpy as np
from  math import *
from turtle import *


def sommet(c,x,y):
    up()
    setpos(x,y)
    down()
    circle(15)
    up()
    setpos(x,y+5)
    write(c,False,align="center",font=("Ariel",10,"normal"))

    

def arc(x,y,z,t,sens):
    if(sens==0):
        setheading(0)
        up()
        setpos(z,t+30)
        left(90)
        down()
        circle(sqrt((x-z)*(x-z)+(y-t)*(y-t))/2, 180)
    else:
        setheading(0)
        up()
        setpos(x,y)
        left(-90)
        down()
        circle(sqrt((x-z)*(x-z)+(y-t)*(y-t))/2, 180)

    
def arcp(x,y,z,t,c):
    if(x<z):
        sens=0
        arc(x,y,z,t,sens)
        up()
        setpos(x+sqrt((x-z)*(x-z)+(y-t)*(y-t))/2,y+sqrt((x-z)*(x-z)+(y-t)*(y-t))/2+30)
    else:
        sens=1
        arc(z,t,x,y,sens)
        up()
        setpos(z+sqrt((x-z)*(x-z)+(y-t)*(y-t))/2,y-sqrt((x-z)*(x-z)+(y-t)*(y-t))/2-20)
    up()
    down()
    write(c,False,align="center",font=("Ariel",10,"normal"))
    up()
    setpos(0,0)
    
clearscreen()



def graph(M):
    """
    Dessiner un graphe à partir d'une matrice d'adjacence
    """
    n=len(M)
    for i in range(n): 
        sommet(i,i*100,50)
    for i in range (n):
        for j in range (n):
            if (M[i][j]!=0):
                arcp(j*100,50,i*100,50,M[i][j])
                



def detec_cycle(M):
    """
    On compare les voisins de chaque sommet.
    M = ((0,1,0,0,0,1),(0,0,1,0,0,1),(0,0,0,1,0,0),(0,0,0,0,1,0),(0,1,0,0,0,0),(0,0,0,0,0,0))

    |1|  2 |  3 |  4 |  5 |  6 |      file = []
    |0|None|None|None|None|None|      file = [1]
    |0|  1 |None|None|None|None|      file = [2,6]
    |0|  1 |  2 |None|None|  1 |      file = [3]
    |0|  1 |  2 |  3 |None|  1 |      file = [4]
    |0|  1 |  2 |  3 |  4 |  1 |      file = [5]
         *              *
      --> 4>1 donc cycle

    Entrée : tuples
    Sortie : str
        
    Tests :
    >>>detec_cycle((0,1,0),(0,0,1),(1,0,0)
    Graphe Cyclique
    >>>detec_cycle(((0,1,0,0,0,1),(0,0,1,0,0,1),(0,0,0,1,0,0),(0,0,0,0,1,0),(0,1,0,0,0,0),(0,0,0,0,0,0)))
    Graphe Acyclique
    """
    file = []
    element = [None for i in range(len(M))]
    file.append(0)
    element[0] = 0
    while len(file) != 0:
        u = file.pop(0)
        for v in voisins(u, M):
            if element[v] == None:
               element[v] = element[u] + 1
               file.append(v)
            elif element[v] <= element[u]:
               return "Graphe Cyclique"
    return "Graphe Acyclique"



def voisins(sommet, graph):
    tmp = []
    for i in range(len(graph)):
      if graph[sommet][i] == 1:
        tmp.append(i)
    return tmp



def same_vect(v1, v2): 
    """
    Vérifie si deux vecteurs sont identiques.
    v1 = (0,1,0,0,0,1)
    v2 = (0,0,0,0,0,0)
    
    Entrée : 2 tuples
    Sortie : bool
    
    Tests :
    >>>v1 = (0,1,0,0,0,1)
    >>>v2 = (0,0,0,0,0,0)
    >>>same_vect(v1, v2)
    False
    >>>v1 = (0,1,0,0,0,1)
    >>>v2 = (0,1,0,0,0,1)
    >>>same_vect(v1, v2)
    True
    """
    for k in range(len(v1)):
        if v1[k] != v2[k]:
            return False
    return True
 
    

def tp_ts(M):
    """
    Renvoie un vecteur ts (planning séquentiel) et un vecteur tp (planning au plus vite) à partir d'une matrice d'adjacence M.
    
    Entrée : tuple
    Sortie : 2 lists
    
    Tests : 
    >>>M = [[0,1,0,0,0,1],[0,0,1,0,0,1],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,1,0,0,0,0],[0,0,0,0,0,0]]
    >>>tp_ts(M)
    ([[2], [3, 4], [1], [0]], [2, 3, 4, 1, 0])
    """
    l = len(M)
    tp = []
    ts = []
    M = np.array(M)
    nul = []
    if (detec_cycle(M) == 'Graphe Acyclique'):
        for n in range(l): #Vecteur nul de la taille de la matrice
            nul.append(0)
        while len(ts) != l :
            tmp = []
            for j in range(l) :  
                if j not in ts and same_vect(M[:,j], nul) :
                    tmp.append(j)
            tp.append(tmp)
            for e in tmp :
                ts.append(e)
            for j in tmp :
                M[j,:]=nul
        return(tp, ts)
    else : 
        return "Veuillez donner un graphe acyclique s'il vous plait!"

    



def afficher(t):
    for i,e in enumerate(t):
        if type(e) is list:
            print(i, ":", *e)
        else:
            print(i, ":", e)



M = ((0,0,0,0,0),(1,0,0,0,0),(0,0,0,1,1),(1,1,0,0,0),(0,0,0,0,0))
#M = ((0,1,0),(0,0,1),(1,0,0))

if (detec_cycle(M) == 'Graphe Acyclique'):
    print(detec_cycle(M))
    tp, ts = tp_ts(M)
    print("\nPlanning au plus vite :")
    afficher(tp)
    print("\nPlanning séquentiel :")
    afficher(ts)
    graph(M)
else :
    print(detec_cycle(M))
    print(tp_ts(M))