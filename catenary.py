#code to get the vertical balance of multiple catenaries
#formulas obtained from http://www.mecapedia.uji.es/calculo_de_la_catenaria_conocidos_los_puntos_de_amarre_y_la_longitud.htm
#hyperbolic functions http://mpmath.org/doc/current/functions/hyperbolic.html
import numpy as np
import math
import matplotlib.pyplot as plt

from mpmath import * #valid for hyperbolic functions


#initialization of distances
HorDif=120 #horizontal distance between extremes [cm]
VerDif=20 #vertical distance between extremes [cm]
S=200 #length of the catenary in cm
w=0.005 #weight per unit length [kg/cm]
vectorX1=np.linspace(0,HorDif,100) #X points of the first catenary


#calculus of vertical descent for equilibrum
def VerticalDescend(L0,Lx,w):

    Y2=-40 #initialization value
    expresion_A=math.sqrt(3)*sqrt((L0**2 - Y2**2)/(Lx**2)-1)

    iter2=1

    F1_1=w/2*(-Y2*coth(expresion_A)+L0)-2*w*L0/3
    F2_1=w/2*(-coth(expresion_A)-(math.sqrt(3)*Y2**2*(csch(expresion_A))**2/((Lx**2)*expresion_A/math.sqrt(3))))

    Y2=Y2-F1_1/F2_1
    F3_1=w/2*(-Y2*coth(expresion_A)+L0)-2*w*L0/3


    while(abs(F1_1-F3_1)>0.0000000001 and abs(F1_1)>0.0001):
   
        #this function states that each point of the catenary must load 1/3 of the total weight
        F1_1=w/2*(-Y2*coth(expresion_A)+L0)-2*w*L0/3
   
        #derivative of F1_1
        F2_1=w/2*(-coth(expresion_A)-(math.sqrt(3)*Y2**2*(csch(expresion_A))**2/((Lx**2)*expresion_A/math.sqrt(3))))
    
        #manual implementation of Newton-Raphson
        Y2=Y2-F1_1/F2_1
        F3_1=w/2*(-Y2*coth(expresion_A)+L0)-2*w*L0/3
        iter2=iter2+1

    return Y2


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
    y= list(map(fun, VectorX)) #it's a list
    y=np.asarray(y)

    return y,x0,y0,c


#calculate the parameters of the initial catenary
y0,x0,y_0,c0= catenary(HorDif, 0, S, vectorX1)
y1,x01,y_1,c1 = catenary(HorDif,0, S, vectorX1)


#calculate the parameters of the final catenary with an animation
VerDif=VerticalDescend(S,HorDif,w)
VerDif_vector=np.linspace(0,float(VerDif),5)

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
    
   
plt.show()
