def check_columnas(sudoku):
    longitud = len(sudoku)
    for indice in range(0, longitud):
        columna = []
        for fila in sudoku:
            if len(fila) >= indice + 1:
                columna.append(fila[indice])
        for numero in columna:
            if columna.count(numero) > 1:
                return False
    return True


### CASOS TEST ###

if __name__ == '__main__':
    ### CASO TEST 1 ###
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    assert check_columnas(correct) == True

    ### CASO TEST 2 ###
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]
    assert check_columnas(incorrect) == False

    ### CASO TEST 3 ###
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]
    assert check_columnas(incorrect2) == False

    ### CASO TEST 4 ###
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]
    assert check_columnas(incorrect3) == True

    ### CASO TEST 5 ###
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    assert check_columnas(incorrect4) == True

    ### CASO TEST 6 ###
    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    assert check_columnas(incorrect5) == True

    ### CASO TEST 7 ###
    irregular = [[1,2,3],
                 [2,3,1]]
    assert check_columnas(irregular) == True

    ### CASO TEST 8 ###
    irregular2 = [[1,2,3],
                 [2,3,1],
                 [3,1]]
    assert check_columnas(irregular2) == True
