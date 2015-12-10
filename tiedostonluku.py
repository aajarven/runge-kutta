# -*- coding: utf-8 -*-
"""
Runge-Kutta -algoritmin toteuttamiseen tarvittavat tiedostonlukufunktiot
Matriisin alkiot erotetaan toisistaan pilkulla, matriisit puolipisteellä. Rivejä, jotka alkavat merkillä # ei huomioida.
Esimerkiksi seuraava tiedosto:
#X0	        V0              M
0., 0.;	    0.	0.;          1
1.,	0.;	    0.,	6.28;       3e-6
tuottaa matriisit
X0= [[0., 0.], [1., 0.,]]
V0= [[0., 0.], [0., 6.28]]
M= [1, 3e-6]
@author: Anni Järvenpää
"""

import numpy as np

"""
Lukee tiedostosta alkuarvomatriisit X0, V0 ja M. Ei huomioi #-merkillä alkavia rivejä.
Toiminnaltaan vastaava kuin lueMatr, mutta sallii kommenttirivit. Tästä syystä tehottomampi.
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
    
"""
Kirjoittaa matriisin tiedostoon
@param: kirjoitettava matriisi
@param: kohdetiedoston nimi
"""
def kirjoitaMatr(matriisi, tiedostonimi):
    tiedosto = open(tiedostonimi, 'w')
    for i in range(matriisi.shape[0]): # rivi
        for j in range(len(matriisi[0][0])): # vektori (kappale)
            for k in range(len(matriisi[0][0][0])): # alkio
                tiedosto.write(str(matriisi[i][0][j][k]))
                if (k != len(matriisi[0][0][0])-1):
                    tiedosto.write(",\t")
            if (j != len(matriisi[0][0])-1):
                tiedosto.write(";\t")
        if(i != matriisi.shape[0]-1):
                tiedosto.write("\n")
    tiedosto.close()

"""
Lukee matriiseja sisältävän matriisin tiedostosta
@param: luettavan tiedoston nimi
"""
def lueMatr(tiedostonimi):
     tiedosto = open(tiedostonimi, 'r')
     rivit = tiedosto.readlines()
     palautus = np.ndarray((len(rivit), len(rivit[0].split(";"))), dtype=object)
     for i in range(len(rivit)):
        matriisit = [m.strip() for m in rivit[i].strip().split(';')]
        for j in range(len(matriisit)):
            try:
                palautus[i][j] = [float(luku.strip()) for luku in matriisit[j].strip().split(',')]
            except ValueError:
                print "Virhe luettaessa tiedoston riviä ",i
                break
            palautus[i][j] = [float(luku.strip()) for luku in matriisit[j].split(',')]
                
     return palautus
     
     