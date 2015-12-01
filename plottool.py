# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import tiedostonluku
import sys

"""
inputfile, x-arvojen sarake, y-arvojen sarake
"""
def main():
    #TODO argumenttitarkastus
    #TODO värit
    #TODO s argumenttina?
    tiedosto = sys.argv[1]
    xSarake = int(sys.argv[2])
    ySarake = int(sys.argv[3])
    data = tiedostonluku.lueMatr(tiedosto)
    varit = matplotlib.cm.rainbow(np.linspace(0, 1, data.shape[0]))
    
    for i in range(data.shape[0]):
        x =  [row[xSarake] for row in data[i]]
        y = [row[ySarake] for row in data[i]]
        plt.scatter(x, y, c=varit[i], s=20)
    plt.show()
    
if __name__ == '__main__':
    main()