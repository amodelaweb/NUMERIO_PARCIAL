#POR SANTIAGO CHAUSTRE Y JUAN CASTAÑEDA
import math
import sympy as sy
import numpy as np
from sympy.functions import exp
import time

x = sy.Symbol('x')
f = exp(-x)

def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(math.factorial(i))*((x-x0)**i)
        i += 1
    #print (p)
    return p
def main():
    starttime = time.time()
    ciclos = 9
    x=5
    func = taylor(f,4,ciclos)
    res= eval(str(func))
    print("\nla aproximacion es: %e " % float(res) )
    endtime = time.time() - starttime
    print ("el tiempo de ejecucion es: ", endtime)

main()
