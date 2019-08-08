#code to get the vertical balance of multiple catenaries
#formulas obtained from http://www.mecapedia.uji.es/calculo_de_la_catenaria_conocidos_los_puntos_de_amarre_y_la_longitud.htm
import numpy as np
import math
import matplotlib.pyplot as plt


#initialization of distances
HorDif=120 #horizontal distance between extremes [cm]
VerDif=20 #vertical distance between extremes [cm]
S=200 #length of the catenary in cm
w=0.005 #weight per unit length
vectorX1=np.linspace(0,HorDif,100) #X points of the catenary


#catenary calculus function
def catenary(HorDif,VerDif,S,VectorX):

    #calculus of x0 and y0 (see the reference web)

    c=3 #initialization

    f1=math.sqrt(S**2 - VerDif**2)/HorDif
    f2=math.sinh(HorDif/(2*c))/HorDif*(2*c)


    while (abs(f2-f1)>0.01):
        c=c+0.01
        f1=math.sqrt(S**2 - VerDif**2)/HorDif
        f2=math.sinh(HorDif/(2*c))/HorDif*(2*c)


    x0=3 #initialization

    f3= c*math.cosh((HorDif-x0)/c) - c*math.cosh(x0/c)

    while(abs(f3-VerDif)>0.1):
        x0=x0+0.01
        f3= c*math.cosh((HorDif-x0)/c) - c*math.cosh(x0/c)


    y0 = VerDif - c*math.cosh((HorDif-x0)/c)

    #generate the y points of the catenary
    fun = lambda vecX : y0 + c * math.cosh((vecX - x0) / c)
    y= list(map(fun, VectorX))

    return y,x0,y0,c


#calculate the parameters of the catenary
y,x0,y0,c= catenary(HorDif, VerDif, S, vectorX1)

#draw the catenary
plt.plot(vectorX1,y)
plt.show()
