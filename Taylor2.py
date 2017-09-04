from sympy import *
from mpmath import *

def main():
     p = taylor(exp, -5, 9)
     print("El resultado de esta aproximacion es %e " % polyval(p[::-1], 0))

main()
