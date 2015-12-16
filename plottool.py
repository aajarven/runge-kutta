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

    nollakoordinaatit = data[:,0]
#    print data
#    print
#    print nollakoordinaatit
    
    x = np.zeros((data.shape[0], data.shape[1]))
    y = np.zeros((data.shape[0], data.shape[1])) 
    plt.figure(figsize=(10,10))
    
    for i in range(data.shape[1]): # kappaleet
        x = np.zeros((data.shape[0], data.shape[1]))
        for j in range(data.shape[0]): # rivit
            koordinaatit = np.subtract(data[j,i],nollakoordinaatit[j])
            x[j] = koordinaatit[xSarake]
            y[j] = koordinaatit[ySarake]
        plt.scatter(x, y, facecolor=varit[i], edgecolor=varit[i], s=1)

    plt.show()
     
    
"""
inputfile, x-arvojen sarake, y-arvojen sarake, plotmode
"""   
if __name__ == '__main__':
    tiedosto = argv[1]
    xSarake = int(argv[2])
    ySarake = int(argv[3])
    data = tiedostonluku.lueMatr(tiedosto)
    varit = matplotlib.cm.rainbow(np.linspace(0, 1, data.shape[1]))
    if (argv[4]=="s" or argv[3]=="simple"):
        simpleplot()
    elif (argv[4]=="t" or argv[3]=="tahti"):
        centerplot()
    plt.savefig(tiedosto+".png")