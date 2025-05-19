# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

x = np.linspace(-2*PI,2*PI,100)


y1 = np.sin(x)

y2 = np.cos(x)

plt.plot(x,y1,'gv-',label='sin(x)')
plt.plot(x,y2,'ro-.',label='cos(x)')

plt.legend(loc='best')

plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Seno y Coseno')

plt.grid()

plt.show()

