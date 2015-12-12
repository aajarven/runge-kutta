# -*- coding: utf-8 -*-

import numpy as np
import math
import sys
import tiedostonluku

G = 4*math.pi**2 # AU^3/(M_sun*a^2)


def rungekutta(f, g, R0, V0, M, dt):
    k1x = f(R0, V0, M) 
    k1y = g(R0, V0, M) 
    k2x = f(R0 + 0.5*dt*k1x, V0 + 0.5*dt*k1y, M)
    k2y = g(R0 + 0.5*dt*k1x, V0 + 0.5*dt*k1y, M)
    k3x = f(R0 + 0.5*dt*k2x, V0 + 0.5*dt*k2y, M)
    k3y = g(R0 + 0.5*dt*k2x, V0 + 0.5*dt*k2y, M)
    k4x = f(R0 + dt*k3x, V0 + dt*k3y, M)
    k4y = g(R0 + dt*k3x, V0 + dt*k3y, M)
    
    R1 = np.add(R0, dt*(k1x + 2*k2x + 2*k3x + k4x)/6)
    V1 = np.add(V0, dt*(k1y + 2*k2y + 2*k3y + k4y)/6)
    return (R1, V1)
    
def dv(R, V, M):
    dv = np.zeros(V.shape)
    for i in range(R.shape[0]):
        for j in range(R.shape[0]):
            if (i != j):
                r = R[i]-R[j]
                m = M[j]
                dv[i] += -G*m*(r)/(np.linalg.norm(r)**3)
    return dv
    
def dr(R, V, M):
    return V

#TODO kunnollinen dokumentaatio
#TODO rakenne järkevämmäksi, mainissa liikaa
"""
parametrit: in-tiedostonimi, t_max, dt, nimi
"""
def main():
    if (len(sys.argv) != 5 or "-h" in sys.argv or "-help" in sys.argv):
        print "\nAnna parametreina alkuarvot sisältävä tekstitiedosto (kukin kappale rivillään, jokaisella rivillä paikat pilkulla erotettuna; nopeudet pilkulla erotettuna; massa), simulaation kesto, aika-askeleen pituus ja output-tiedostonimi. Yksiköinä AU, yr, M_☉.\n\nOhjelma tulostaa kappaleiden paikat riveittäin ajanhetkillä dt, 2dt, 3dt, ... tiedostoon output-tiedostonimi-X.txt ja vastaavat nopeudet tiedostoon output-tiedostonimi-V.txt. Output-tiedostoissa yksittäisen kappaleen koordinaatit on erotettu pilkulla ja kappaleet puolipisteellä.\n"
        exit()
    
    tiedostonimi = str(sys.argv[1])
    matriisit = tiedostonluku.lueXVM(tiedostonimi)
    tup = (np.array(matriisit[0]), np.array(matriisit[1]))
    M = np.array(matriisit[2])
    t=0.
    t_max = float(sys.argv[2])
    dt = float(sys.argv[3])
    nimi = sys.argv[4]
    outX = np.ndarray((int(math.ceil(t_max/dt)), 1), dtype=object)
    outV = np.ndarray((int(math.ceil(t_max/dt)), 1), dtype=object)
    outRivi = 0
    
    for outRivi in range(outX.shape[0]):
        tup = rungekutta(dr, dv, tup[0], tup[1], M, dt)
        outX[outRivi][0]= tup[0] # X
        outV[outRivi][0] = tup[1] # V  
        t += dt
    
    tiedostonluku.kirjoitaMatr(outX, nimi+"-X.txt")
    tiedostonluku.kirjoitaMatr(outV, nimi+"-V.txt")
    
    
if __name__ == '__main__':
    main()