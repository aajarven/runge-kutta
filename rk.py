# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import tiedostonluku

G = 4*math.pi**2 # AU^3/(M_sun*a^2)


def rungekutta(f, g, R0, V0, M, dt):
    koko = R0.shape
    R1 = np.copy(R0)
    V1 = np.copy(V0)
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
                R1[i] = np.add(R1[i], dt*(k1x + 2*k2x + 2*k3x + k4x)/6)
                V1[i] = np.add(V1[i], dt*(k1y + 2*k2y + 2*k3y + k4y)/6)
                
    return (R1, V1)
    
def dv(r, v, m):
    return -G*m*(r)/(len(r)**3)
    
def dr(r, v, m):
    return v

#TODO kunnollinen dokumentaatio
#TODO rakenne järkevämmäksi, mainissa liikaa
"""
parametrit: in-tiedostonimi, t_max, dt, nimi
"""
def main():
    if (len(sys.argv) != 5):
        print "Anna parametreina alkuarvot sisältävä tekstitiedosto (kukin kappale rivillään, jokaisella rivillä paikat pilkulla erotettuna; nopeudet pilkulla erotettuna; massa), simulaation kesto, aika-askeleen pituus ja output-tiedostonimi. Yksiköinä AU, yr, M_☉"
    
    tiedostonimi = str(sys.argv[1])
    matriisit = tiedostonluku.lueXVM(tiedostonimi)
    tup = (np.array(matriisit[0]), np.array(matriisit[1]))
    M = np.array(matriisit[2])
    t=0
    t_max = float(sys.argv[2])
    dt = float(sys.argv[3])
    nimi = sys.argv[4]
    
    outX = np.ndarray((math.floor((t_max-t)/dt)+1, 1), dtype=object)
    outV = np.ndarray((math.floor((t_max-t)/dt)+1, 1), dtype=object)
    outRivi = 0
    
    while (t<t_max):
        tup = rungekutta(dr, dv, tup[0], tup[1], M, dt)
        X = tup[0]
        V = tup[1]
        #plt.plot(X[0][0], X[0][1], 'ro') #TODO plottaus ei kuulu tänne
        #plt.plot(X[1][0], X[1][1], 'bo')    
        t += dt
        
        outX[outRivi][0]= X
        outV[outRivi][0] = V
        outRivi = outRivi + 1        
        
    #plt.show()
    print outX        
    tiedostonluku.kirjoitaMatr(outX, nimi+"-X.txt")
    tiedostonluku.kirjoitaMatr(outV, nimi+"-V.txt")
    
    
if __name__ == '__main__':
    main()