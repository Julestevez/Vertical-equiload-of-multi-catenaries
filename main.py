#code to get the vertical balance of multiple catenaries
#formulas obtained from http://www.mecapedia.uji.es/calculo_de_la_catenaria_conocidos_los_puntos_de_amarre_y_la_longitud.htm
#hyperbolic functions http://mpmath.org/doc/current/functions/hyperbolic.html
#code to get the vertical balance of multiple catenaries
#formulas obtained from http://www.mecapedia.uji.es/calculo_de_la_catenaria_conocidos_los_puntos_de_amarre_y_la_longitud.htm
#hyperbolic functions http://mpmath.org/doc/current/functions/hyperbolic.html
import numpy as np
import math
import matplotlib.pyplot as plt

from mpmath import *
from VerticalDescend import VerticalDescend #import the functions of other files
from catenary import catenary


#initialization of distances
HorDif=120 #horizontal distance between extremes [cm]
VerDif=20 #vertical distance between extremes [cm]
S=200 #length of the catenary in cm
w=0.005 #weight per unit length [kg/cm]
vectorX1=np.linspace(0,HorDif,100) #X points of the first catenary


#TWO CATENARIES, not balanced
#************************************#
#calculate the parameters of the initial catenary
""" y0,x0,y_0,c0= catenary(HorDif, 0, S, vectorX1)
y1,x01,y_1,c1 = catenary(HorDif,0, S, vectorX1)


#calculate the parameters of the final catenary with an animation
VerDif=VerticalDescend(S,HorDif,w)
VerDif_vector=np.linspace(0,float(VerDif),5)


#ANIMATION OF THE BALANCED CATENARIES
for i in range(0,4):
    y2,x2,y_2,c2= catenary(HorDif, VerDif_vector[i], S, vectorX1)
    y3,x03,y_3,c3 = catenary(HorDif,-VerDif_vector[i], S, vectorX1)

    #draw the catenary
    plt.cla()
    plt.xlim(-5,250)
    plt.ylim(-100,5)
    plt.plot(vectorX1,y0,'b')
    plt.plot(vectorX1+HorDif,y1,'b')

    plt.plot(vectorX1,y2,'r')
    plt.plot(vectorX1+HorDif,y3+VerDif_vector[i],'r') 
    plt.pause(0.1)
    
   
plt.show() """
#END OF TWO CATENARIES



#THREE CATENARIES
#*********************************
y4,x04,y_4,c4 = catenary(HorDif,0, S, vectorX1)
y5,x05,y_5,c5 = catenary(HorDif,0, S, vectorX1)
y6,x06,y_6,c6 = catenary(HorDif,0, S, vectorX1)

#calculate the parameters of the final catenary with an animation
VerDif=VerticalDescend(S,HorDif,w)
VerDif_vector=np.linspace(0,float(VerDif),5)

#ANIMATION OF THE BALANCED CATENARIES
for i in range(0,4):
    y7,x07,y_7,c7 = catenary(HorDif, VerDif_vector[i], S, vectorX1)
    y8,x08,y_8,c8 = catenary(HorDif, 0, S, vectorX1) #two nodes of the catenary in the middle do not have height difference
    y9,x09,y_9,c9 = catenary(HorDif, -VerDif_vector[i], S, vectorX1)

    #draw the catenary
    plt.cla()
    plt.xlim(-5,360)
    plt.ylim(-150,5)
    plt.plot(vectorX1,y4,'b')
    plt.plot(vectorX1+HorDif,y5,'b')
    plt.plot(vectorX1+2*HorDif,y6,'b')

    plt.plot(vectorX1,y7,'r')
    plt.plot(vectorX1+HorDif,y8+VerDif_vector[i],'r') 
    plt.plot(vectorX1+2*HorDif,y9+VerDif_vector[i],'r')
    plt.pause(0.1)
    
   
plt.show()
