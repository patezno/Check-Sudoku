def numeros_en_rango(sudoku):
    for fila in sudoku:
        for elemento in fila:
            if elemento not in range(1, len(fila) + 1):
                    return False
    return True

### CASOS TEST ###

if __name__ == '__main__':
    ### CASO TEST 1 ###
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    assert numeros_en_rango(correct) == True

    ### CASO TEST 2 ###
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]
    assert numeros_en_rango(incorrect) == True

    ### CASO TEST 3 ###
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]
    assert numeros_en_rango(incorrect2) == True

    ### CASO TEST 4 ###
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]
    assert numeros_en_rango(incorrect3) == False

    ### CASO TEST 5 ###
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    assert numeros_en_rango(incorrect4) == False

    ### CASO TEST 6 ###
    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    assert numeros_en_rango(incorrect5) == False

    ### CASO TEST 7 ###
    irregular = [[1,2,3],
                 [2,3,1]]
    assert numeros_en_rango(irregular) == True

    ### CASO TEST 8 ###
    irregular2 = [[1,2,3],
                 [2,3,1],
                 [3,1]]
    assert numeros_en_rango(irregular2) == False
