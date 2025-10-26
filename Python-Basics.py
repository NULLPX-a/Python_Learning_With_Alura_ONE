#                           ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
#                           ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
#                           ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
#                           ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
#                           ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
#                           ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#                                                                                
#                             ██████╗  █████╗ ███████╗██╗ ██████╗███████╗    ██╗   
#                             ██╔══██╗██╔══██╗██╔════╝██║██╔════╝██╔════╝    ██║   
#                             ██████╔╝███████║███████╗██║██║     ███████╗    ██║   
#                             ██╔══██╗██╔══██║╚════██║██║██║     ╚════██║    ╚═╝   
#                             ██████╔╝██║  ██║███████║██║╚██████╗███████║    ██╗   
#                             ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚══════╝    ╚═╝   


#Aprendiendo a codear en Python con el curso de Alura ONE

#Variables y tipos de datos
#existen varios tipos de datos en Python, los mas comunes son:
# - Enteros (int): Números sin decimales
# - Flotantes (float): Números con decimales
# - Cadenas de texto (str): Texto encerrado entre comillas
# - Booleanos (bool): Valores de verdad, pueden ser True o False
#Para crear una variable en Python, simplemente asignamos un valor a un nombre de variable usando el signo igual (=)

nombre = "Juan"
edad = 25
estatura = 1.75
es_estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("Es estudiante:", es_estudiante)

#Podemos verificar el tipo de dato de una variable usando la función type()
print("Tipo de dato de 'nombre':", type(nombre))
print("Tipo de dato de 'edad':", type(edad))
print("Tipo de dato de 'estatura':", type(estatura))
print("Tipo de dato de 'es_estudiante':", type(es_estudiante))

#También podemos convertir entre tipos de datos usando las funciones int(), float(), str() y bool()
edad_como_cadena = str(edad)
print("Edad como cadena:", edad_como_cadena)
print("Tipo de dato de 'edad_como_cadena':", type(edad_como_cadena))
estatura_como_entero = int(estatura)
print("Estatura como entero:", estatura_como_entero)
print("Tipo de dato de 'estatura_como_entero':", type(estatura_como_entero))
es_estudiante_como_entero = int(es_estudiante)
print("Es estudiante como entero:", es_estudiante_como_entero)
print("Tipo de dato de 'es_estudiante_como_entero':", type(es_estudiante_como_entero))

#Operaciones básicas
#Podemos realizar operaciones matemáticas básicas con variables numéricas
a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b       

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)

#También podemos concatenar cadenas de texto usando el operador +
saludo = "Hola, " + nombre + "!"
print(saludo)

#Y podemos usar f-strings para formatear cadenas de texto de manera más sencilla
mensaje = f"Mi nombre es {nombre}, tengo {edad} años y mido {estatura} metros."
print(mensaje)

#Hay diferente funciones en f-strings que nos permiten dar formato a los datos, por ejemplo:
pi = 3.141592653589793
mensaje_pi = f"El valor de pi con dos decimales es: {pi:.2f}"
print(mensaje_pi)
#En este caso, usamos :.2f para indicar que queremos mostrar el número con dos decimales.
#pero .2f solo corta los decimales, no redondea. Si queremos redondear, podemos usar la función round()
pi_redondeado = round(pi, 2)
mensaje_pi_redondeado = f"El valor de pi redondeado a dos decimales es: {pi_redondeado}"
print(mensaje_pi_redondeado)

#En este caso, usamos round(pi, 2) para redondear el valor de pi a dos decimales antes de mostrarlo.

#Otra funcion en f-strings es el uso de :> y :< para alinear texto a la derecha o izquierda respectivamente.
nombre_derecha = f"Nombre alineado a la derecha: {nombre:>10}"
nombre_izquierda = f"Nombre alineado a la izquierda: {nombre:<10}"
print(nombre_derecha)
print(nombre_izquierda)
#En este caso, usamos :>10 para alinear el nombre a la derecha en un espacio de 10 caracteres,
#y usamos :<10 para alinear el nombre a la izquierda en un espacio de 10 caracteres.    

