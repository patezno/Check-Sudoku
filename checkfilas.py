def check_filas(sudoku):
    for lista in sudoku:
        for numero in lista:
            if lista.count(numero) > 1:
                return False
    return True

### CASOS TEST ###

if __name__ == '__main__':
    ### CASO TEST 1 ###
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    assert check_filas(correct) == True

    ### CASO TEST 2 ###
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]
    assert check_filas(incorrect) == False

    ### CASO TEST 3 ###
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]
    assert check_filas(incorrect2) == False

    ### CASO TEST 4 ###
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]
    assert check_filas(incorrect3) == True

    ### CASO TEST 5 ###
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    assert check_filas(incorrect4) == True

    ### CASO TEST 6 ###
    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    assert check_filas(incorrect5) == True

    ### CASO TEST 7 ###
    irregular = [[1,2,3],
                 [2,3,1]]
    assert check_filas(irregular) == True

    ### CASO TEST 8 ###
    irregular2 = [[1,2,3],
                 [2,3,1],
                 [3,1]]
    assert check_filas(irregular2) == True
