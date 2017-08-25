#PUNTO1 DEL PARCIAL
#NEWTON RHAPSON MODIFICADO 
from math import *
from sympy import *
import time

fx= "x**2 +2*x +1" 
gx="x**2 +2*x +1" 
g1x=str(diff(gx))
g2x=str(diff(g1x))
x=1
tolerancia=0.0001
N=50
i=1
print('iteracion\tg(f(x))\t\terror\t\tderivada')
starttime = time.time()
while i<=N:
    d= float(eval(g1x))
    if d != 0:
        x0= x - (((eval(gx)*d))/((d**2)-eval(gx)*eval(g2x))) #EL PRINCIPAL CAMBIO SE HIZO AQUI
    er=abs(x0-x)
    print("%d\t\t%.5f\t\t%.5f\t\t%.5f"%(i,x0,er,d));
    if er<tolerancia:
        endtime = time.time() - starttime
        print("La raiz es %.6f"%x0)
        print ("El tiempo de ejecucion fue : %.4f Sg" % endtime)
        break
    i=i+1
    x=x0
if i>=N:
    print("El metodo no converge ")
