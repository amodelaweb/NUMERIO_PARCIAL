#PUNTO2 DE ANALISIS NUMERICO, METODO DE LA SECANTW 
# POR SANTIAGO CHAUSTRE PERDOMO Y JUAN CASTAÑEDA
#METODO DE LA RECANTE 

def main():
   x0 = input('Ingrese x0 ')
   xant = input ('Ingrese x-1 ')
   tol = input ('Ingrese la tolerancia ')
   error = 1E10
   fx = "2**x-1.3"

   fx0 = eval(fx,{'x':x0})
   fxant = eval (fx,{'x':xant})
   x = x0 - ((fx0 * (xant - x0 )) /  (fxant - fx0))
       
   while abs(error) > tol and eval(fx,{'x':x}) != 0:
       #CODIGO
       fx0 = eval(fx,{'x':x0})
       fxant = eval (fx,{'x':xant})
       x = x0 - ((fx0 * (xant - x0 )) /  (fxant - fx0))
       error = abs ((x0-x)/x)*100
       xant = x0
       x0 = x 
   print("El resultado es : %.4f"%x)     
main()
