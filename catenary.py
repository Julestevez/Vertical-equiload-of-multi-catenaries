#code to get the vertical balance of multiple catenaries
import numpy as np
import math
import matplotlib.pyplot as plt


#initialization of distances
HorDif=120; xB2=120 #horizontal distance between extremes
S=200 #length of the catenary
w=0.005 #weight per unit length
vectorX1=np.linspace(0,HorDif,100) #create a vector of X values
vectorX2=np.linspace(0,xB2,100)
#yB1=descenso(Sab,xB1,w);



def catenary(HorDif,VerDif,S,VectorX):
    c=3 #initialization

    f1=math.sqrt(S^2 - VerDif^2)/HorDif
    f2=math.sinh(HorDif/(2*c))/HorDif*(2*c)


    while (abs(f2-f1)>0.01):
        c=c+0.01
        f1=math.sqrt(S^2 - VerDif^2)/HorDif
        f2=math.sinh(HorDif/(2*c))/HorDif*(2*c)

    print("ya esta 3")
    #ahora consigo la x0, y0
    y0=c

    #consigo x0
    x0=3#initialization

    f3= c*math.cosh((HorDif-x0)/c) - c*math.cosh(x0/c)

    while(abs(f3-VerDif)>0.1):
        x0=x0+0.01
        f3= c*math.cosh((HorDif-x0)/c) - c*math.cosh(x0/c)

    print("ya esta 2")
    #hallo y0
    y0 = VerDif - c*math.cosh((HorDif-x0)/c)

    #dibujo la catenaria
    y=y0 + c*math.cosh((VectorX-x0)/c)

    return y,x0,y0,c


#catenarias sin equilibrar
y,x0,y0,c= catenary(HorDif, 0, S, vectorX1)


print("ya esta")
