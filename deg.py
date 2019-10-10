# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:27:46 2019

@author: tinou
"""

import numpy as np
import math

n = int(input("Taille du graphe: "))
m = np.zeros((n,n))
    
for i in range(n):
    for j in range(n):
        v = 2
        while ((v != 0) and (v != 1)):
            print("m[{0},{1}] = ".format(i,j), end=" ")
            v = int(input())
            #v = int(input("m[{0},{1}] = ".format(i,j)))
            if ((v != 0) and (v != 1)):
                print("La valeur doit être 0 ou 1")
            else :
                m[i,j] = int(v)

print('\n'.join([''.join(['{:2d}'.format(int(item)) for item in row]) for row in m]))

#degre
deg_in = np.zeros((n))
deg_out = np.zeros((n))
for i in range(n):
    for j in range(n):
        deg_in[i] += m[i,j]
        deg_out[j] += m[i,j]
for i in range(n):
    print(f"Sommet{i+1}: degre >= {int(deg_in[i])} degre <= {int(deg_out[j])}")
    
deg = np.zeros((n))
for i in range(n):
    deg[i] = deg_in[i] + deg_out[i]
print
