#       Ejercicios de Matriz inversa

# Ejercicio#1

import numpy as np

# Definir la matriz A
A = np.array([[1, 3],
              [2, 4]])

# Calcular la inversa de A
A_inversa = np.linalg.inv(A)

print("Inversa de la matriz A:")
print(A_inversa)


# Ejercicio#2

import numpy as np

# Definir la matriz A
A = np.array([[1, 2, 1],
              [1, 3, 2],
              [1, 0, 1]])

# Calcular la inversa de A
A_inversa = np.linalg.inv(A)

print("Inversa de la matriz A:")
print(A_inversa)


# Ejercicio#3

import numpy as np

# defnir la matriz A
A = np.array([[1, 1, 1],
              [1, 2, 3],
              [0, 1, 1]])

# calcular la inversa de A
A_inversa = np.linalg.inv(A)

print("Inversa de la matriz A:")
print(A_inversa)

# Ejercicio#4

import numpy as np

# Definir la matriz A
A = np.array([[1, 2, 2],
              [1, 3, 1],
              [1, 3, 2]])

# Calcular la inversa de A
A_inversa = np.linalg.inv(A)

print("Inversa de la matriz A:")
print(A_inversa)

# Ejercicio#5

import numpy as np

# Definir la matriz A
A = np.array([[3, 1, 2],
              [2, 1, 2],
              [1, 2, 2]])

# Calcular la inversa de A
A_inversa = np.linalg.inv(A)

print("Inversa de la matriz A:")
print(A_inversa)


# Ejercicio#6

import numpy as np

# Definir la matriz A
A = np.array([[1, 2, 3],
              [1, 1, 2],
              [1, 1, 0]])

# Calcular la inversa de A
A_inversa = np.linalg.inv(A)

# Redondear los valores de la matriz inversa a un decimal
A_inversa_redondeada = np.round(A_inversa, decimals=1)

print("Inversa de la matriz A (valores redondeados a un decimal):")
print(A_inversa_redondeada)

#Ejercicio 7
import sympy as sp

# Definir la matriz
A = sp.Matrix([[0, -2], [1, 5]])

# Calcular la inversa de A
A_inversa = A.inv()

print("Matriz Inversa de A:")
print(A_inversa)


#Ejercicio 8

import sympy as sp

#Definir la matriz A

A = sp.Matrix([[-3, 2],
               [0, 8]])

#Calcular La inversa de la matriz A

A_inversa = A.inv()

print("Matriz A:\n", A)
print("\nInversa de la matriz A:\n", A_inversa)


#Ejercicio 9

#averigua si la matriz A tiene inversa
import numpy as np
matriz = np.array([[1, 1, -2],
                   [2, 1, 3],
                   [1, 3, -1]])
determinante = np.linalg.det(matriz)
if determinante != 0:
    print("La matriz tiene inversa.")
    inversa = np.linalg.inv(matriz)
    print("La inversa de la matriz es:")
    print(inversa)
else:
    print("La matriz no tiene inversa.")


#Ejercicio 10

import numpy as np

matriz = np.array([[1, 2, -3],
                   [2, 3, -5],
                   [3, 5, 2]])

determinante = np.linalg.det(matriz)

if determinante != 0:
    print("La matriz tiene inversa.")
    inversa = np.linalg.inv(matriz)
    print("La inversa de la matriz es:")
    print(inversa)
else:
    print("La matriz no tiene inversa.")


#Ejercicio 11

#averigua si la matriz A tiene inversa
import numpy as np
matriz = np.array([[1, 1, -2],
                   [2, 1, 3],
                   [1, 3, -1]])
determinante = np.linalg.det(matriz)
if determinante != 0:
    print("La matriz tiene inversa.")
    inversa = np.linalg.inv(matriz)
    print("La inversa de la matriz es:")
    print(inversa)
else:
    print("La matriz no tiene inversa.")


# Ejercicio 12

    import numpy as np

    matriz = np.array([[1, 1, 1],
                       [3, 2, 1],
                       [2, 1, 0]])

    determinante = np.linalg.det(matriz)

    print("El determinante de la matriz es:", determinante)

    if determinante != 0:
        print("La matriz no tiene inversa.")

    else:
        print("La matriz tiene inversa.")
    inversa = np.linalg.inv(matriz)
    print(inversa)

#       Ejercicios de la matriz Transpuesta

#Ejercicio1.

# Definir la matriz original
matriz_original = [
    [1, 2],
    [3, 4]
]
# Calcular la matriz transpuesta
matriz_transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

# Imprimir la matriz transpuesta
print("La matriz transpuesta del ejercicio#1 es:")
for fila in matriz_transpuesta:
    print(fila)


#Ejercicio2.

#Definir la matriz original
matriz_original = [
    [0, 1],
    [0, 0]
]

# Calcular la matriz transpuesta
matriz_transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

# Imprimir la matriz transpuesta
print("La matriz transpuesta del ejercicio#2 es:")
for fila in matriz_transpuesta:
    print(fila)


#Ejercicio3.

# Definir la matriz original
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la matriz transpuesta
matriz_transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

# Imprimir la matriz transpuesta
print("La matriz transpuesta del ejercicio#3 es:")
for fila in matriz_transpuesta:
 print(fila)


#Ejercicio4.

# Definir la matriz original
matriz_original = [
    [0, -2, 0],
    [0, 0, 7],
    [1, 0, 0]
]

# Calcular la matriz transpuesta
matriz_transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

# Imprimir la matriz transpuesta
print("La matriz transpuesta del ejercicio#4 es:")
for fila in matriz_transpuesta:
 print(fila)


#Ejercicio5.

# Definir la matriz original
matriz_original = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Calcular la matriz transpuesta
matriz_transpuesta = [[fila[i] for fila in matriz_original] for i in range(len(matriz_original[0]))]

# Imprimir la matriz transpuesta
print("La matriz transpuesta del ejercicio#5 es:")
for fila in matriz_transpuesta:
    print(fila)

#Ejercicio6.
# Definir la matriz original
matriz_original = [
    [0, -7/2, 3, 1/4],
    [1, -1, -2, 5/4]
]

# Imprimir el mensaje con el nuevo resultado de la matriz transpuesta
print("La matriz transpuesta del ejercicio#6 es:")
for i in range(len(matriz_original[0])):
    fila_transpuesta = [fila[i] for fila in matriz_original]
    print(fila_transpuesta)


#Ejercicio7

import numpy as np

# Definir la matriz A
A = np.array([[-12, -9],
              [-5, 0]])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)


#Ejercicio8

import numpy as np

# Definir la matriz A
A = np.array([[0, -6],
              [7, 0]])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)


#Ejercicio9

import numpy as np

# Definir la matriz A
A = np.array([[0, -2, 0],
              [0, 0, 7],
              [1, 0, 0]])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)


#Ejercicio10

import numpy as np

# Definir la matriz A
A = np.array([[1, 0, 7],
              [0, 3, 4],
              [1, 5, 0]])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)


#Ejercicio11

import numpy as np

# Definir la matriz A
A = np.array([3, 0, -7])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)


#Ejercicio12

import numpy as np

# Definir la matriz A
A = np.array([[1, 3],
              [-9, 1/4],
              [3, -6],
              [1/10, 0]])

# Calcular la transpuesta de A
A_transpuesta = np.transpose(A)

print("Transpuesta de la matriz A:")
print(A_transpuesta)
