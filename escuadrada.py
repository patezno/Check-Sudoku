def es_cuadrada(columna):
    for fila in columna:
        if len(fila) != len(columna):
            return False
    return True

### CASOS TESTS ###

if __name__ == '__main__':

    ### CASO TEST 1 ###
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    assert es_cuadrada(correct) == True

    ### CASO TEST 2 ###
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]
    assert es_cuadrada(incorrect) == True

    ### CASO TEST 3 ###
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]
    assert es_cuadrada(incorrect2) == True

    ### CASO TEST 4 ###
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]
    assert es_cuadrada(incorrect3) == True

    ### CASO TEST 5 ###
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    assert es_cuadrada(incorrect4) == True

    ### CASO TEST 6 ###
    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    assert es_cuadrada(incorrect5) == True

    ### CASO TEST 7 ###
    irregular = [[1,2,3],
                 [2,3,1]]
    assert es_cuadrada(irregular) == False

    ### CASO TEST 8 ###
    irregular2 = [[1,2,3],
                 [2,3,1],
                 [3,1]]
    assert es_cuadrada(irregular2) == False
