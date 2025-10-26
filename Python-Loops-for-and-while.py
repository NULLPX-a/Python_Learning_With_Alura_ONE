#                           ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
#                           ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
#                           ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
#                           ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
#                           ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
#                           ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#                                                                                
#                           ██╗      ██████╗  ██████╗ ██████╗ ███████╗           
#                           ██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝           
#                           ██║     ██║   ██║██║   ██║██████╔╝███████╗           
#                           ██║     ██║   ██║██║   ██║██╔═══╝ ╚════██║           
#                           ███████╗╚██████╔╝╚██████╔╝██║     ███████║           
#                           ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝           

#Python Loops - Curso de Python con Alura ONE

#estructuras de repetición: for y while
#Los bucles o estructuras de repetición nos permiten ejecutar un bloque de código varias veces.


#Bucle for
#El bucle for nos permite iterar sobre una secuencia (como una lista, una tupla o una cadena de texto) y ejecutar un bloque de código para cada elemento de la secuencia.
#La sintaxis básica de un for en Python es la siguiente:
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)
#En este ejemplo, el bucle for itera sobre cada elemento de la lista frutas y asigna cada elemento a la variable fruta en cada iteración. Luego, imprime un mensaje indicando que le gusta esa fruta. 
#El resultado será:
#Me gusta la manzana
#Me gusta la banana
#Me gusta la cereza

#También podemos usar la función range() para generar una secuencia de números y usarla en un bucle for.
for i in range(5):
    print("Número:", i)
#En este ejemplo, el bucle for itera sobre los números del 0 al 4 (5 no está incluido) y los imprime uno por uno.
#El resultado será:
#Número: 0
#Número: 1
#Número: 2
#Número: 3
#Número: 4

#----███████████████████████████████████----

#Bucle while
#El bucle while nos permite ejecutar un bloque de código mientras se cumpla una condición determinada.
#La sintaxis básica de un while en Python es la siguiente:
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
#En este ejemplo, el bucle while ejecuta el bloque de código mientras la variable contador sea menor que 5. En cada iteración, imprime el valor del contador y luego lo incrementa en 1.
#El resultado será:
#Contador: 0
#Contador: 1
#Contador: 2
#Contador: 3
#Contador: 4


#Es importante asegurarse de que la condición del while eventualmente se vuelva falsa, de lo contrario, el bucle continuará ejecutándose indefinidamente, lo que se conoce como un bucle infinito.
#Podemos usar la instrucción break para salir de un bucle antes de que la condición se vuelva falsa.
numero = 0
while True:
    print("Número:", numero)
    numero += 1
    if numero >= 5:
        break
#En este ejemplo, el bucle while se ejecuta indefinidamente debido a la condición True. Sin embargo, usamos la instrucción break para salir del bucle cuando el número alcanza 5.
#El resultado será:
#Número: 0
#Número: 1
#Número: 2
#Número: 3
#Número: 4 



#También podemos usar la instrucción continue para saltar a la siguiente iteración del bucle.
for i in range(10):
    if i % 2 == 0:
        continue
    print("Número impar:", i)
#En este ejemplo, el bucle for itera sobre los números del 0 al 9. Si el número es par (es decir, si el resto de dividirlo por 2 es 0), usamos continue para saltar a la siguiente iteración del bucle. Si el número es impar, lo imprimimos.
#El resultado será:
#Número impar: 1
#Número impar: 3
#Número impar: 5
#Número impar: 7
#Número impar: 9
#Con estas estructuras de repetición, podemos automatizar tareas y procesar datos de manera eficiente en Python.
