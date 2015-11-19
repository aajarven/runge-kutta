# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

G = 1 # gravitaatiovakio, TODO
dt = 0.1

def rungekutta(f, g, R0, V0, M):
    koko = R0.shape
    R1 = R0
    V1 = R0
    for i in range(koko[0]):
        for j in range(koko[1]):
            if (i != j):              
                dx = R0[j]-R0[i]
                dy = V0[j]-V0[i]
                m = M[j]

                k1x = f(dx, dy, m) 
                k1y = g(dx, dy, m) 
                k2x = f(dx + 0.5*dt*k1x, dy + 0.5*dt*k1y, m)
                k2y = g(dx + 0.5*dt*k1x, dy + 0.5*dt*k1y, m)
                k3x = f(dx + 0.5*dt*k2x, dy + 0.5*dt*k2y, m)
                k3y = g(dx + 0.5*dt*k2x, dy + 0.5*dt*k2y, m)
                k4x = f(dx + dt*k3x, dy + dt*k3y, m)
                k4y = g(dx + dt*k3x, dy + dt*k3y, m)

                R1[i] = R1[i]+ dt*(k1x + 2*k2x + 2*k3x + k4x)/6
                V1[i] = R1[i] + dt*(k1y + 2*k2y + 2*k3y + k4y)/6

    return (R1, V1)

def dv(r, v, m):
    return -G*m*(r)/len(r)**3
    
def dr(r, v, m):
    return v

def len(vec):
    return (np.dot(vec, vec))**0.5

X0 = np.array([[0, 0], [1, 0]])
V0 = np.array([[0, 0], [0, 5]])
M = [200.0, 1.0]
t = 0 
t_max = 1

tup = (X0, V0)
print(tup[0])
plt.clf()
plt.cla()


while(t<t_max):
    tup = rungekutta(dr, dv, tup[0], tup[1], M)
    
    plt.plot(tup[0][0][0], tup[0][0][1], 'ro')
    plt.plot(tup[0][1][0], tup[0][0][1], 'bo')
    plt.axis((0, 40, 0, 40))
    #plt.show()
    
    t = t + dt

plt.show()
print(tup[0])