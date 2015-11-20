# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time

G = 1 # au^3/(M_earth day^2)  (astronomical units cubed per Earth mass day squared)
dt = 1

# AU
# d

def rungekutta(f, g, R0, V0, M):
    koko = R0.shape
    R1 = R0
    V1 = R0
    for i in range(koko[0]):
        for j in range(koko[0]):
            if (i != j):              
                x = R0[i]-R0[j]
                y = V0[i]
                m = M[j]

                k1x = f(x, y, m) 
                k1y = g(x, y, m) 
                k2x = f(x + 0.5*dt*k1x, y + 0.5*dt*k1y, m)
                k2y = g(x + 0.5*dt*k1x, y + 0.5*dt*k1y, m)
                k3x = f(x + 0.5*dt*k2x, y + 0.5*dt*k2y, m)
                k3y = g(x + 0.5*dt*k2x, y + 0.5*dt*k2y, m)
                k4x = f(x + dt*k3x, y + dt*k3y, m)
                k4y = g(x + dt*k3x, y + dt*k3y, m)

                R1[i] += dt*(k1x + 2*k2x + 2*k3x + k4x)/6
                V1[i] += dt*(k1y + 2*k2y + 2*k3y + k4y)/6
    return (R1, V1)

def dv(r, v, m):
    return -G*m*(r)/(len(r)**3)
    
def dr(r, v, m):
    return v

def len(vec):
    return (np.dot(vec, vec))**0.5

X0 = np.array([[0.0, 0.0], [2.0, 1.0]])
V0 = np.array([[0.0, 0.0], [0.0, 0.0]])
print(X0[0])
print(X0[1])
print(X0[1]-X0[0])
print(dv(X0[1]-X0[0], V0[1], 1))

M = [20.0, 1.0]
t = 0 
t_max = 10
out = []
i = 0

tup = (np.copy(X0), np.copy(V0))
#print(tup[0])
plt.clf()
plt.cla()


while(t<t_max):
    tup = rungekutta(dr, dv, tup[0], tup[1], M)
    out.append(tup[0])
    plt.plot(tup[0][0][0], tup[0][0][1], 'ro')
    plt.plot(tup[0][1][0], tup[0][0][1], 'bo')
    #plt.axis((0, 40, 0, 40))
    plt.show()
    t = t + dt

#print(out)
plt.show()
print(X0[0])
print(X0[1])
print(X0[1]-X0[0])
print(dv(X0[1]-X0[0], V0[1], 1))

print(out)
#print(tup[0])