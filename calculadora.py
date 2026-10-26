"""
Calculador Básica
Descripción: Programa en Python de una calculadora básica
caluladora.py
""" 

def suma(a, b):
   return a + b

def resta(a, b):
   return a - b

if __name__ == "__main__":
   #Referencias
   num1 = 10
   num2 = 8
   
   #Impresión de valores
   print(f"El resultado de la suma es: {suma(num1, num2)}")
   print(f"El resultado de la resta es: {resta(num1, num2)}")