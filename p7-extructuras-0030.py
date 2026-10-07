# ============================================
# EJERCICIOS DE PYTHON
# Nombre: Darrell Cepeda
# Numero de Control: 0030
# ============================================


# ============================================
# CASO 1: IF
# Ejemplo 1
# ============================================

edad = 18

if edad >= 18:
    print("Ejemplo 1 - Eres mayor de edad")


# Ejemplo 2
numero = 10

if numero > 0:
    print("Ejemplo 2 - El numero es positivo")


# ============================================
# CASO 2: IF - ELSE
# Ejemplo 1
# ============================================

edad = 16

if edad >= 18:
    print("Ejemplo 1 - Puedes votar")
else:
    print("Ejemplo 1 - No puedes votar")


# Ejemplo 2
numero = 7

if numero % 2 == 0:
    print("Ejemplo 2 - El numero es par")
else:
    print("Ejemplo 2 - El numero es impar")


# ============================================
# CASO 3: IF - ELIF - ELSE
# Ejemplo 1
# ============================================

calificacion = 85

if calificacion >= 90:
    print("Ejemplo 1 - Excelente")
elif calificacion >= 70:
    print("Ejemplo 1 - Aprobado")
else:
    print("Ejemplo 1 - Reprobado")


# Ejemplo 2
# ============================================

dia = 3

if dia == 1:
    print("Ejemplo 2 - Lunes")
elif dia == 2:
    print("Ejemplo 2 - Martes")
elif dia == 3:
    print("Ejemplo 2 - Miercoles")
else:
    print("Ejemplo 2 - Otro dia")


# ============================================
# CASO 4: FOR
# Ejemplo 1
# ============================================

print("Ejemplo 1 - Numeros del 1 al 5")

for numero in range(1, 6):
    print(numero)


# Ejemplo 2
# ============================================

print("Ejemplo 2 - Tabla del 5")

for numero in range(1, 11):
    print("5 x", numero, "=", 5 * numero)


# ============================================
# CASO 5: WHILE
# Ejemplo 1
# ============================================

print("Ejemplo 1 - Numeros del 1 al 5")

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1


# Ejemplo 2
# ============================================

print("Ejemplo 2 - Cuenta regresiva")

numero = 5

while numero >= 1:
    print(numero)
    numero = numero - 1

print("Fin de los ejercicios")

print("Programa ejecutado por Cepeda Darrell NC 0030")