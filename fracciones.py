#CLASE
class Fraction():
    ##ATRIBUTOS##
    numerator = 0
    denominator = 1
    ##FIN##

    ##CONSTRUCTOR##
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    ##FIN##

    ##MÉTODOS##
    def multiplication(self,other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        print("\nLa multiplicación da como resultado:",numerator,"/",denominator)

    def division(self,other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        print("\nLa división da como resultado:",numerator,"/",denominator)

    def addition(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)+(other.numerator*self.denominator)
            print("\nLa suma da como resultado:",numerator,"/",denominator)
        else:
            numerator = self.numerator + other.numerator
            print("\nLa suma da como reusltado:",numerator,"/",self.denominator)

    def subtraction(self,other):
        if(self.denominator != other.denominator):
            denominator = self.denominator * other.denominator
            numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
            print("\nLa resta da como resultado:",numerator,"/",denominator)
        else:
            numerator = self.numerator - other.numerator
            print("\nLa resta da como resultado:",numerator,"/",self.denominator)
    ##FIN##
            

##VARIABLES##
numerator_1 = 0
numerator_2 = 0
denominator_1 = 0
denominator_2 = 0
fraction1 = 0
fraction2 = 0
opcion = 0
    
##PEDIR AL USUARIO##
numerator_1 = int(input("Numerador de la primera fracción"))
denominator_1 = int(input("Denominador de la primera fracción:"))
numerator_2 = int(input("Numerador de la segunda fracción: "))
denominator_2 = int(input("Denominador de la segunda fracción:"))

fraction1 = Fraction(numerator_1, denominator_1)
print("Primera fracción =",fraction1.numerator,"/",fraction1.denominator)
fraction2 = Fraction(numerator_2, denominator_2)
print("Segunda fracción =",fraction2.numerator,"/",fraction2.denominator)

##MOSTRAR EN PANTALLA##
print("\n ᲼᲼ ᲼᲼ ᲼FRACCIONES ᲼᲼ ᲼᲼ ᲼\n")
print("En caso de suma, su opción será:(+)")
print("En caso de resta, su opción será:(-)")
print("En caso de multiplicación, su opción será:(*)")
print("En caso de división, su opción será:(/)\n")
print("===============================================\n")
opcion = input("Ingrese la opción (+ - * /):")

##OPCIONES - IF ELSE## 
if(opcion =='+'):
    fraction1.addition(fraction2)
elif(opcion =='-'):
    fraction1.subtraction(fraction2)
elif(opcion =='*'):
    fraction1.multiplication(fraction2)
elif(opcion =='/'):
    fraction1.division(fraction2)
else:
    print("Por favor, ingrese una opción correcta.")
