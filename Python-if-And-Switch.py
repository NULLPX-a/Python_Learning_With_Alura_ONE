#                       ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗                        
#                       ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║                        
#                       ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║                        
#                       ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║                        
#                       ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║                        
#                       ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                        
#                                                                                                    
#                        ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
#                       ██╔════╝██╔═══██╗████╗  ██║██╔══██╗██║╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
#                       ██║     ██║   ██║██╔██╗ ██║██║  ██║██║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
#                       ██║     ██║   ██║██║╚██╗██║██║  ██║██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
#                       ╚██████╗╚██████╔╝██║ ╚████║██████╔╝██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
#                        ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝


# Python Basics - Curso de Python con Alura ONE

# Estructuras de control: if, and, or, match siendo el equivalente de switch

#Estructura condicional if
#La estructura condicional if nos permite ejecutar un bloque de código solo si se cumple una condición determinada.
#La sintaxis básica de un if en Python es la siguiente:
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
#En este ejemplo, si la variable edad es mayor o igual a 18, se imprimirá "Eres mayor de edad.". Si no, se imprimirá "Eres menor de edad.".

#Tambien podemos usar elif para agregar condiciones adicionales
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")
#En este ejemplo, se evaluarán las condiciones en orden. Si la nota es mayor o igual a 90, se imprimirá "Excelente". Si no, se evaluará la siguiente condición, y así sucesivamente.

#----███████████████████████████████████----

#Operadores lógicos: and, or, not
#Los operadores lógicos nos permiten combinar múltiples condiciones en una estructura condicional.
#-------------------------------
#|  a |  b  | a and b | a or b |
#|----|-----|---------|--------|
#| T  |  T  |    T    |   T    |
#| T  |  F  |    F    |   T    |
#| F  |  T  |    F    |   T    |
#| F  |  F  |    F    |   F    |
#-------------------------------
#- and: Devuelve True si ambas condiciones son verdaderas.
#- or: Devuelve True si al menos una de las condiciones es verdadera.

edad = 25
tiene_identificacion = True
if edad >= 18 and tiene_identificacion:
    print("Puedes entrar al club.")
else:
    print("No puedes entrar al club.")
    
#En este ejemplo, se verifican dos condiciones: si la edad es mayor o igual a 18 y si la persona tiene identificación. Solo si ambas condiciones son verdaderas, se imprimirá "Puedes entrar al club.".

promedio = 75
asistencia = 80
if promedio >= 70 or asistencia >= 75:
    print("Aprobaste el curso.")
else:
    print("No aprobaste el curso.")
#En este ejemplo, se verifican dos condiciones: si el promedio es mayor o igual a 70 o si la asistencia es mayor o igual a 75. Si al menos una de las condiciones es verdadera, se imprimirá "Aprobaste el curso.".

 
 
#Estructura match (equivalente a switch)
#La estructura match nos permite comparar una variable contra múltiples valores posibles y ejecutar el bloque de código correspondiente al valor que coincida.
#La sintaxis básica de un match en Python es la siguiente
dia = "martes"
match dia:
    case "lunes":
        print("Hoy es lunes.")
    case "martes":
        print("Hoy es martes.")
    case "miércoles":
        print("Hoy es miércoles.")
    case _:
        print("No es un día válido.")
#En este ejemplo, se compara la variable dia contra varios valores posibles. Si dia es "martes", se imprimirá "Hoy es martes.". Si no coincide con ninguno de los casos especificados

