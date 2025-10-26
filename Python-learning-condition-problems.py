#Bruno gestiona un pequeño comercio y quiere saber qué producto tuvo el mejor desempeño de ventas el mes pasado. Registró la cantidad vendida de dos productos: manzanas y plátanos. Ahora, necesita escribir un programa que identifique y muestre cuál de ellos tuvo más ventas.

#Crea un programa que reciba el número de ventas de los dos productos y muestre un mensaje indicando cuál de ellos vendió más. Si las cantidades son iguales, muestra un mensaje diciendo que hubo un empate.

#Salida esperada:
#Digite la cantidad de manzanas vendidas: 4
#Digite la cantidad de plátanos vendidas: 9
#las plátanos tuvieron más ventas.

Manzanas_vendidas = int(input("Digite la cantidad de manzanas vendidas: "))
Platanos_vendidas = int(input("Digite la cantidad de plátanos vendidas: "))

if Manzanas_vendidas > Platanos_vendidas:
    print("Las manzanas tuvieron más ventas.")
elif Platanos_vendidas > Manzanas_vendidas:
    print("Los plátanos tuvieron más ventas.")
else:
    print("Hubo un empate en las ventas.")




#Lucas trabaja en TI y necesita garantizar que la temperatura de una sala de servidores no supere los 25°C. Quiere un programa que reciba la temperatura actual como entrada y, si es necesario, muestre un mensaje de alerta.

#Salida esperada:
#Digite la temperatura actual: 30
#Alerta: Temperatura por encima del límite_permitido.

Temperatura_actual = float(input("Digite la temperatura actual: "))

if Temperatura_actual > 25:
    print("Alerta: Temperatura por encima del límite permitido.")
else:
    print("La temperatura está dentro del rango permitido.")


#Camila está organizando un proyecto y necesita calcular el tiempo total necesario para concluir tres actividades: A, B y C. Sin embargo, si alguna actividad tiene un número de días negativo, el código debe avisar que los valores ingresados son inválidos y no calcular el total.

#Escribe un programa que reciba el número de días de tres actividades y muestre el tiempo total del proyecto. Si algún valor es negativo, muestra un mensaje informando el error.

#Salida esperada:
#Informe los días para la actividad A: 8
#Informe los días para la actividad B: 6
#Informe los días para la actividad C: -7
#ERROR: Los dias no pueden ser negativos.

Dias_actividad_A = int(input("Informe los días para la actividad A: "))
Dias_actividad_B = int(input("Informe los días para la actividad B: "))
Dias_actividad_C = int(input("Informe los días para la actividad C: "))

if Dias_actividad_A < 0 or Dias_actividad_B < 0 or Dias_actividad_C < 0:
    print("ERROR: Los dias no pueden ser negativos.")
else:
    Tiempo_total = Dias_actividad_A + Dias_actividad_B + Dias_actividad_C
    print("El tiempo total del proyecto es de", Tiempo_total, "días.")




#Anna Júlia está creando un sistema para calcular el Índice de Masa Corporal (IMC) y proporcionar recomendaciones básicas. El programa debe recibir el peso y la altura de una persona y mostrar el valor del IMC, además de indicar si está por debajo del peso, con peso normal o por encima del peso. Crea un programa que reciba el peso (en kg) y la altura (en metros) y calcule el IMC usando la fórmula: IMC = peso / (altura ** 2)Luego, muestra el valor del IMC y un mensaje indicando si está por debajo del peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) o por encima del peso (IMC >= 25).

#Salida esperada:
#Digite su peso en (kg): 60
#Digite su altura en (m): 1.65
#Su IMC es: 22.04
#Usted tiene un peso normal.

Peso = float(input("Digite su peso en (kg): "))
Altura = float(input("Digite su altura en (m): "))
IMC = Peso / (Altura ** 2)
print("Su IMC es: {:.2f}".format(IMC))
if IMC < 18.5:
    print("Usted está por debajo del peso.")
elif 18.5 <= IMC < 25:
    print("Usted tiene un peso normal.")
else:
    print("Usted está por encima del peso.")


#  ___                           _                     
# / _ \ _ __   ___ _ __ __ _  __| | ___  _ __ ___  ___ 
#  | | | '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__/ _ \/ __|
#  |_| | |_) |  __/ | | (_| | (_| | (_) | | |  __/\__ \
# \___/| .__/ \___|_|  \__,_|\__,_|\___/|_|  \___||___/
#  |   |_|_   __ _(_) ___ ___  ___                     
#  |   / _ \ / _` | |/ __/ _ \/ __|                    
#  |__| (_) | (_| | | (_| (_) \__ \                    
# _____\___/ \__, |_|\___\___/|___/                    
#            |___/                                     


#Laura está desarrollando un sistema para saber si una persona tiene derecho a recibir un beneficio social. Para eso, la persona debe cumplir las siguientes condiciones:
# Tener ingresos menores o iguales a $2000.
# Tener al menos un hijo o hija.

#crea un programa que reciba los ingresos mensuales y la cantidad de hijos de una persona, y diga si tiene derecho al beneficio social.

Ingresos_mensuales = float(input("Digite sus ingresos mensuales: "))
Cantidad_hijos = int(input("Digite la cantidad de hijos: "))

if Ingresos_mensuales <= 2000 and Cantidad_hijos >= 1:
    print("Usted tiene derecho al beneficio social.")
else:
    print("Usted no tiene derecho al beneficio social.")


#Una empresa evalua a sus empleados con base en dos criterios
# Puntuacion de desempeño (0 a 10)
# Años Trabajados

#Reglas:
# Si la puntuacion es mayor o igual a 7:
#    Si trabajo mas de 5 años: "elegible para ascenso"
#    Si trabajo 5 años o menos: "Buen desempeño, sigue asi"

# si la puntiuacion es menor a 7: "Necesita mejoprar"

Puntuacion_desempeno = float(input("Digite la puntuacion de desempeño (0 a 10): "))
Anios_trabajados = int(input("Digite los años trabajados: "))

if Puntuacion_desempeno >= 7:
    if Anios_trabajados > 5:
        print("Elegible para ascenso.")
    else:
        print("Buen desempeño, sigue así.")
else:
    print("Necesita mejorar.")


#Estas desarrollando un pequeño juego. El usuario ingresa un numero entero y el programa debe evaluar lo siguiente:
# Si el numero es divisible por 3 y 5: mostrar "Numero Magico!"
# si el numero solo es divisible por 3: mostrar "Divisible por 3"
# si el numero solo es divisible por 5: mostrar "Divisible por 5"
# si no es divisible por ninguno: mostrar "No es un numero magico"

Numero = int(input("Ingrese un número entero: "))

if Numero % 3 == 0 and Numero % 5 == 0:
    print("Número Mágico!")
elif Numero % 3 == 0:
    print("Divisible por 3")
elif Numero % 5 == 0:
    print("Divisible por 5")
else:
    print("No es un número mágico")


#Una escuela otroga becas segun tres criterios:
# Ingreso Familiar mensual
# Promedio del estudiante
# Asistencia (en porcentaje)

#Reglas:
# Si el ingreso es menor a $1,5000 y el promedio es mayor a 8.0 y la asistencia es al menos 90% -> "Beca completa"
# Si el ingreso es menor a $2,5000 y el promedio es mayor a 7.0 y la asistencia es al menos 85% -> "Media beca"
# En otros casos -> "No es elegible para beca"

Ingreso_familiar = float(input("Digite el ingreso familiar mensual: "))
Promedio_estudiante = float(input("Digite el promedio del estudiante: "))
Asistencia = float(input("Digite la asistencia (en porcentaje): "))

if Ingreso_familiar < 1500 and Promedio_estudiante > 8.0 and Asistencia >= 90:
    print("Beca completa")
elif Ingreso_familiar < 2500 and Promedio_estudiante > 7.0 and Asistencia >= 85:
    print("Media beca")
else:
    print("No es elegible para beca")

# Un sistema de transporte cobra según la edad del pasajero y la distancia recorrida:

#Menores de 6 años: Viajan gratis.
#De 6 a 18 años:
#   Hasta 20 km: $1.50
#   Más de 20 km: $2.50
#Mayores de 18:
#   Hasta 20 km: $2.50
#   Más de 20 km: $4.00
#Crea un programa que reciba la edad y distancia, y muestre el valor a pagar.

Edad = int(input("Digite la edad del pasajero: "))
Distancia = float(input("Digite la distancia a recorrer (en km): "))
if Edad < 6:
    print("Viaja gratis.")
elif 6 <= Edad <= 18:
    if Distancia <= 20:
        print("Valor a pagar: $1.50")
    else:
        print("Valor a pagar: $2.50")
else:
    if Distancia <= 20:
        print("Valor a pagar: $2.50")
    else:
        print("Valor a pagar: $4.00")


# Una empresa evalúa su trimestre con base en:
#
#   Ingresos totales
#   Gastos totales
#   Número de nuevos clientes

#C lasificación:
#
#   Si ingresos - gastos > $10,000 y más de 50 nuevos clientes → "Trimestre Excelente"
#   Si ingresos - gastos > $5,000 y al menos 20 clientes → "Trimestre Bueno"
#   Si ingresos - gastos > 0 → "Trimestre Regular"
#   Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"

Ingresos_totales = float(input("Digite los ingresos totales del trimestre: "))
Gastos_totales = float(input("Digite los gastos totales del trimestre: "))
Nuevos_clientes = int(input("Digite el número de nuevos clientes: "))

Beneficio = Ingresos_totales - Gastos_totales

if Beneficio > 10000 and Nuevos_clientes > 50:
    print("Trimestre Excelente")
elif Beneficio > 5000 and Nuevos_clientes >= 20:
    print("Trimestre Bueno")
elif Beneficio > 0:
    print("Trimestre Regular")
else:
    print("Trimestre Deficitario")

