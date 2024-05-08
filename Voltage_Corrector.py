# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:16:25 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format
import matplotlib.pylab as pylab #for qol features, in this case text size manipulation
#Make sure to replace my file path with your own.
#same general layout as XRD grapher. Make sure to replace my file path with your own.

def Voltage_corrector(filenamesin,filenamesout,Voffset,cycle): #txt is true if dealing with a txt file, and false if dealing with a csv
#currentDependence: True if current is on the y axis.   
#sample input: Voltage_corrector(['0Al_03_CV_C01','1Al_03_CV_C01','2Al_03_CV_C01','4_1_24_03_CV_C01','4_13_24 0025AlCl_03_CV_C01','4_13_24 0025AlNO3_03_CV_C01'],['0 Al vs RHE cycle 1','1 Al vs RHE cycle 1','2 Al vs RHE cycle 1','hexagonal particles vs RHE cycle 1','Cl Anion particles vs RHE cycle 1','NO3 Anion particles vs RHE cycle 1'],0.925,1)

    
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    cycles=[C1,C2,C3,C4,C5,C6,C7]
    i=0
    while(i < len(filenamesin)):
        datalistX[i],datalistY[i],cycles[i]=np.loadtxt(fname=r"C:\Users\isaac\OneDrive\Documents\aluminum substituted hematite reduction project\Electrochemical tests\txt files\5_1 and 5_2 CVs\5_2"+"/" + filenamesin[i] + ".txt", skiprows=1, unpack=True,
                                             usecols=(0,1,2))
                
        i2 = 0
        disposableX = []
        disposableY = []
        if cycle == None:
            disposableX = datalistX[i]
            disposableY = datalistY[i]
        else:
            while(i2<len(datalistX[i])): #cycle selector functionality
                if cycles[i][i2] == cycle: #cycles[i][i2] < cycle+0.5 and cycles[i][i2]>cycle-0.5:
                    disposableX = np.append(disposableX,datalistX[i][i2])
                    disposableY = np.append(disposableY,datalistY[i][i2])
               
                i2 = i2 + 1
        #return disposableX
        
        
        
        np.savetxt(filenamesout[i],np.transpose([disposableX+Voffset,disposableY]),header='E (V) i (mA)')
        
        i = i + 1