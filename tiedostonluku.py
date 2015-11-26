# -*- coding: utf-8 -*-
"""
Runge-Kutta -algoritmin toteuttamiseen tarvittavat tiedostonlukufunktiot

@author: Anni Järvenpää
"""

"""
Lukee tiedostosta matriisit X0, V0 ja M.
Matriisin alkiot erotetaan toisistaan pilkulla, matriisit puolipisteellä. Rivejä, jotka alkavat merkillä # ei huomioida.
Esimerkiksi seuraava tiedosto:
#X0	        V0              M
0., 0.;	    0.	0.;          1
1.,	0.;	    0.,	6.28;       3e-6
tuottaa matriisit
X0= [[0., 0.], [1., 0.,]]
V0= [[0., 0.], [0., 6.28]]
M= [1, 3e-6]
"""
def lueXVM(tiedostonimi):
    f = open(tiedostonimi)
    rivit = f.readlines()
    X = []
    V = []
    M = []
    rivinro = 0
    for rivi in rivit:
        if (len(rivi)>0 and rivi[0] != '#'):
            matriisit = [m.strip() for m in rivi.split(';')]
            if(len(matriisit) < 3):
                print 'virhe annetussa tiedostossa rivillä "'+rivi+'"'
            else:
                X.append([float(luku.strip()) for luku in matriisit[0].split(',')])
                V.append([float(luku.strip()) for luku in matriisit[1].split(',')])
                M.append(float(matriisit[2].strip()))
        rivinro = rivinro + 1
    return [X, V, M]