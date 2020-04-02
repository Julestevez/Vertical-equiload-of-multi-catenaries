#calculus of vertical descent for equilibrum

import math
import numpy as np
from mpmath import *

def VerticalDescend(L0,Lx,w):

    Y2=-40 #initialization value
    expresion_A=math.sqrt(3)*math.sqrt((L0**2 - Y2**2)/(Lx**2)-1)

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