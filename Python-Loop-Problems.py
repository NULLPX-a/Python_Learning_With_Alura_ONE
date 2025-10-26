#Ana está desarrollando un programa que necesita procesar una lista de 5 nombres de clientes para generar informes mensuales. Para ello, necesita escribir un programa que recorra la lista de nombres y muestre cada cliente.

nombres_clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]

for nombre in nombres_clientes:
    print("Cliente:", nombre)

#se usa el Loop "for" porque se recorre una lista con un numero definido de elementos. mientras que while se usa cuando no se sabe cuantas veces se va a repetir una accion.

#----███████████████████████████████████----

#André está probando una nueva función en el backend de Buscante que procesa datos en un bucle. Durante las pruebas, se dio cuenta de que el sistema dejó de responder y sospecha que el problema está en un bucle infinito.

# contador = 0
# while contador < 10:
#   print("Procesando datos...")

#¿Cuál es el problema del código de André y cómo resolverlo?

contador = 0
while contador < 10:
    print("Procesando datos...")
    contador += 1  
    
# Incrementar el contador para evitar un bucle infinito, asegurando que la condición eventualmente se vuelva falsa.

#----███████████████████████████████████----

#Marcos está desarrollando un programa para mostrar un mensaje de bienvenida repetidamente en la consola, como parte de una campaña de marketing de su plataforma llamada Buscante. Quiere asegurarse de que el mensaje se muestre 5 veces.

#Ayuda a Marcos a escribir un programa que muestre el mensaje: "¡Bienvenido a Buscante!" el número exacto de veces que necesita.

#salida esperada:
#¡Bienvenido a Buscante!
#¡Bienvenido a Buscante!
#¡Bienvenido a Buscante!
#¡Bienvenido a Buscante!

for i in range(5):
    print("¡Bienvenido a Buscante!")

#----███████████████████████████████████----

#Estás recibiendo una lista de valores que representan los productos de tu tienda virtual y te gustaría calcular la suma total de esos productos para entender el desempeño financiero semanal.
valores = [10, 20, 30, 40, 50]
#Crea un programa para implementar la suma.
#salida esperada
#la suma total de los ingresos es: 150
sumaValores = 0
for valor in valores:
    sumaValores += valor

print(f"La suma total de los ingresos es: {sumaValores}")

#----███████████████████████████████████----

#Ana está desarrollando su portafolio para exhibir los proyectos de Python que ha completado. Ella organizó una lista con el nombre de cada proyecto, pero se dio cuenta de que algunos elementos pueden estar ausentes, apareciendo como None:

proyectos = ["sitio web", "juego", "análisis de datos", None, "aplicativo móvil"]

#Crea un programa que ayude a Ana a recorrer la lista de proyectos y muestre los nombres de los proyectos válidos. Si encuentra un elemento None, el programa debe mostrar el mensaje: "Proyecto ausente".

#Salida esperada:
# Sitio web
# juego
# analisis de datos
# proyecto ausente
# aplicativo movil

for proyectoCheck in proyectos:
    if type(proyectoCheck) != type("."):
        print("proyecto ausente")
    else:
        print(proyectoCheck)
        

#----███████████████████████████████████----

#José está desarrollando una funcionalidad en el sistema de Buscante para interrumpir la búsqueda tan pronto como se encuentre un libro específico. La lista de libros ya registrados en el sistema es la siguiente:

libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]

#Ayuda a José a crear un programa que recorra la lista y muestre el mensaje "Libro encontrado: <nombre del libro>" tan pronto como se encuentre el libro "El Hobbit". Después de encontrar el libro, el programa debe detener inmediatamente la búsqueda, sin verificar los libros restantes.

#Salida esperada:
# Libro encontrado: El Hobbit

for libro in libros:
    if libro == "El Hobbit":
        print("Libro encontrado:", libro)
        break

#----███████████████████████████████████----


# Estás desarrollando un sistema de control de inventario para Buscante. Uno de los requisitos es verificar la cantidad de ejemplares de un libro en inventario y continuar vendiendo hasta que el inventario se agote. Siempre que se realiza una venta, el sistema debe informar al usuario y actualizar la cantidad disponible.

# Crea un programa que simule las ventas de un libro con el inventario inicial de 5 ejemplares. El programa debe mostrar el mensaje "¡Venta realizada! Inventario restante: <cantidad>" con cada venta y, al final, mostrar el mensaje "Inventario agotado".

# Salida esperada:
## ¡Venta realizada! Inventario restante: 4
## ¡Venta realizada! Inventario restante: 3
## ¡Venta realizada! Inventario restante: 2
## ¡Venta realizada! Inventario restante: 1
## ¡Venta realizada! Inventario restante: 0
## Inventario agotado

inventario = 5

while inventario > 0:

    inventario -= 1
    
    if inventario > 0:
        print("¡Venta realizada! Inventario restante: " + str(inventario))
    else:
        print("Inventario Agotado")


#----███████████████████████████████████----

#Aline está implementando una funcionalidad que muestra mensajes personalizados para los clientes durante una promoción especial de su nueva librería. El sistema debe mostrar un mensaje de cuenta regresiva personalizado para cada número de 10 a 1, y al final mostrar el mensaje: "¡Aprovecha la promoción ahora!".

# Crea un programa que utilice un bucle for para mostrar los siguientes mensajes:

#Para números pares, muestra: "Faltan solo <número> segundos - ¡No pierdas esta oportunidad!".
#Para números impares, muestra: "La cuenta continúa: <número> segundos restantes.".
#Al final de la cuenta, muestra el mensaje: "¡Aprovecha la promoción ahora!".

#Salida esperada:
# Faltan solo 10 segundos - ¡No pierdas esta oportunidad!
# La cuenta continúa: 9 segundos restantes.
# Faltan solo 8 segundos - ¡No pierdas esta oportunidad!
# La cuenta continúa: 7 segundos restantes.
# Faltan solo 6 segundos - ¡No pierdas esta oportunidad!
# La cuenta continúa: 5 segundos restantes.
# Faltan solo 4 segundos - ¡No pierdas esta oportunidad!
# La cuenta continúa: 3 segundos restantes.
# Faltan solo 2 segundos - ¡No pierdas esta oportunidad!
# La cuenta continúa: 1 segundos restantes.
# ¡Aprovecha la promoción ahora!

for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f"Faltan solo {segundos} segundos - ¡No pierdas esta oportunidad!")
    else:
        print(f"La cuenta continúa: {segundos} segundos restantes.")
    
print("¡Aprovecha la promoción ahora!")


#----███████████████████████████████████----

#Ana está implementando un sistema de filtrado de libros en Buscante. La funcionalidad debe recorrer una lista de libros y mostrar el nombre de cada libro disponible en stock. Sin embargo, si el libro está agotado, debe ser ignorado durante la iteración.

libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]

#Crea un programa que ayude a Ana a mostrar solamente los libros que tienen stock disponible, en el formato: "Libro disponible: <nombre del libro>".
#Salida esperada:
# Libro disponible: 1984
# Libro disponible: El Principito
# Libro disponible: Orgullo y Prejuicio

for libro in libros:
    if libro["stock"] == 0:
        continue
    print("Libro disponible:", libro["nombre"])

#----███████████████████████████████████----


#João está desarrollando un sistema de registro para un sitio de lectura. Necesita asegurarse de que los usuarios #ingresen un nombre de usuario y una contraseña válidos. Las reglas son las siguientes:

#El nombre de usuario debe tener al menos 5 caracteres.
#La contraseña debe tener al menos 8 caracteres.
#João quiere que el sistema siga solicitando la información hasta que ambas condiciones se cumplan. Cuando el usuario 

#ingresa datos válidos, el programa debe mostrar el mensaje: "¡Registro realizado con éxito!".
#Crea un programa que implemente esta lógica usando un bucle while.

#Salida esperada:
# Digite su nombre de usuario: user
# Digite su contraseña: 123
# El nombre de usuario debe tener al menos 5 caracteres.
# Digite su nombre de usuario: usuario123
# Digite su contraseña: 123
# La contraseña debe tener al menos 8 caracteres.
# Digite su nombre de usuario: usuario123
# Digite su contraseña: contraseña123
# ¡Registro realizado con éxito!
    
while True:
    nombre_usuario = input("Digite su nombre de usuario: ")
    contraseña = input("Digite su contraseña: ")
    
    if len(nombre_usuario) < 5:
        print("El nombre de usuario debe tener al menos 5 caracteres.")
    elif len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    else:
        print("¡Registro realizado con éxito!")
        break


