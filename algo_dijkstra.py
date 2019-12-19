# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:54:20 2019

@author: Estelle
"""


import numpy as np
            
def Init(d, sdeb):
    n = len(d)
    for i in range(n):
        d[i] = np.Infinity
    d[sdeb] = 0
    
def chercher(d, s): 
    mini = np.Infinity
    sommet = -1
    n = len(d)
    for i in range(n):
        if s[i] < 1:
            if d[i] < mini:
                mini = d[i]
                sommet = i
    return sommet

def maj(i, d, s, M):
    n = len(d)
    for j in range(n):
        if M[i][j] != np.Infinity :
            if s[j] <1 :
                d[j] = min(d[j], d[i]+M[i][j])
            
def fin(s):
    r = 1
    n = len(s)
    for i in range(n):
        if(s[i]<1):
            r = 0
    return r

def djk(M, deb):
    n = len(M)
    d = np.zeros(n)
    s = np.zeros(n)
    ch = np.zeros(n)
    Init(d,deb)
    while(fin(s) == 0):
        i = chercher(d, s)
        s[i] = 1
        maj(i, d, s, M)
    af(ch, M, 0, sdeb)
    return d


def af(ch, M, i, sdeb):
    k = i  
    j = k
    while k != sdeb:
        print(k, end='',flush=True)
        k = int(ch[k])
        print('--(',M[j][k],')-->', end='', flush=True)
        j = k
    print(sdeb)


M = (
     (0,-3,0,3,0),
     (-3,0,0,2,4),
     (0,0,0,0,1),
     (3,2,0,0,-4),
     (0,4,0,-4,0))
sdeb = 2
print(djk(M,sdeb))
