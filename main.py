from checkcolumnas import check_columnas
from checkfilas import check_filas
from escuadrada import es_cuadrada
from numerosenrango import numeros_en_rango

def es_correcto(sudoku, test):
    if es_cuadrada(sudoku) and numeros_en_rango(sudoku) and check_filas(sudoku) and check_columnas(sudoku):
        print("El sudoku del caso test " + str(test) + " es correcto")
    else:
        print("El sudoku del caso test " + str(test) + " es incorrecto")

### CASOS TEST ###

### CASO TEST 1 ###
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

es_correcto(correct, 1)

### CASO TEST 2 ###
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,2]]

es_correcto(incorrect, 2)

### CASO TEST 3 ###
incorrect2 = [[1,2,3,4],
              [2,3,1,2],
              [4,1,2,3],
              [2,3,1,4]]

es_correcto(incorrect2, 3)

### CASO TEST 4 ###
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

es_correcto(incorrect3, 4)

### CASO TEST 5 ###
incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

es_correcto(incorrect4, 5)

### CASO TEST 6 ###
incorrect5 = [ [1, 1.5],
               [1.5, 1]]

es_correcto(incorrect5, 6)

### CASO TEST 7 ###
irregular = [[1,2,3],
             [2,3,1]]

es_correcto(irregular, 7)

### CASO TEST 8 ###
irregular2 = [[1,2,3],
             [2,3,1],
             [3,1]]

es_correcto(irregular2, 8)
