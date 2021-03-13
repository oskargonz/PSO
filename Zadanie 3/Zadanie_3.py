# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:10:47 2020

@author: Asus
"""

import numpy as np
import math
import matplotlib.pyplot as plt

omega_zero = 10
omega = np.zeros(21)
output = np.zeros(21)

for i in range(len(omega)):
    omega[i] = i * omega_zero

for i in range(len(omega)):
    Re = (omega_zero / ((omega_zero **2 + omega[i] **2))) **2
    Im = (-omega[i] / ((omega_zero **2 + omega[i] **2))) ** 2
    output[i] = math.sqrt(Re + Im)
    
plt.plot(omega, output)
plt.show()