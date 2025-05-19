# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:57:17 2025

@author: ALUMNO
"""

import numpy as np

def cuadratica(a,b,c):
    if a==0:
        print('Error')
        return None
    d = b**2-4*a*c
    if d<0:
        print('Error')
        return None
    else:
        x1 = -b+np.sqrt(d)/(2*a)
        x2 = -b-np.sqrt(d)/(2*a)
    return x1,x2

print(cuadratica(1,2,1))