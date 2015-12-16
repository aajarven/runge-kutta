# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tiedostonluku
from sys import argv

#TODO: tämä on rumaa
tiedosto = ""
xSarake = 0
ySarake = 1
data = []
varit = []

matplotlib.rcParams.update({'font.size': 22})

#TODO argumenttitarkastus
#TODO värit
#TODO s argumenttina?
def simpleplot():
    for i in range(data.shape[1]):
        x =  [row[xSarake] for row in data[:,i]]
        y =  [row[ySarake] for row in data[:,i]]
        plt.scatter(x, y, facecolor=varit[i], edgecolor=varit[i], s=1)
    plt.show()
    
def centerplot():
    #print data
    #print
#    print data[0,:] # ensimmäinen rivi
#    print data[:,0] # ensimmäisen kappaleen koordinaatit
#    print data.shape[0] # rivien määrä
#    print data.shape[1] # kappaleiden määrä    

    nollakoordinaatit = tiedostonluku.lueMatr(tiedosto+"-mkp.txt")
    #print nollakoordinaatit[1]
    #print
#    print data
#    print
#    print nollakoordinaatit
    
    x = np.zeros((data.shape[0], data.shape[1]))
    y = np.zeros((data.shape[0], data.shape[1])) 
    plt.figure(figsize=(10,10))
    
    for i in range(data.shape[1]): # kappaleet
        x = np.zeros((data.shape[0], data.shape[1]))
        for j in range(data.shape[0]): # rivit
            #print i,", ",j
            #print nollakoordinaatit[j][0]
            #print type(nollakoordinaatit[j][i])
            #print
            #print data[j,i]
            #print type(data[j,i])
            koordinaatit = np.subtract(data[j,i], nollakoordinaatit[j][0])
            x[j] = koordinaatit[xSarake]
            y[j] = koordinaatit[ySarake]
        plt.scatter(x, y, facecolor=varit[i], edgecolor=varit[i], s=1)

    axes = plt.gca()
    axes.set_xlim([-80, 80])
    axes.set_ylim([-80, 80])
    plt.show()
     
    
"""
inputfile, x-arvojen sarake, y-arvojen sarake, plotmode
"""   
if __name__ == '__main__':
    tiedosto = argv[1]
    xSarake = int(argv[2])
    ySarake = int(argv[3])
    data = tiedostonluku.lueMatr(tiedosto+".txt")
    varit = matplotlib.cm.rainbow(np.linspace(0, 1, data.shape[1]))
    if (argv[4]=="s" or argv[3]=="simple"):
        simpleplot()
    elif (argv[4]=="t" or argv[3]=="tahti"):
        centerplot()
    plt.savefig(tiedosto+".png")