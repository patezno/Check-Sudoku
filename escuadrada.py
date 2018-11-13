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
    if es_cuadrada(correct):
        print("El caso test 1 correct funciona")
    else:
        print("El caso test 1 correct no funciona")

    ### CASO TEST 2 ###
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]
    if es_cuadrada(incorrect):
        print("El caso test 2 incorrect funciona")
    else:
        print("El caso test 2 incorrect no funciona")

    ### CASO TEST 3 ###
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]
    if es_cuadrada(incorrect2):
        print("El caso test 3 incorrect2 funciona")
    else:
        print("El caso test 3 incorrect2 no funciona")

    ### CASO TEST 4 ###
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]
    if es_cuadrada(incorrect3):
        print("El caso test 4 incorrect3 funciona")
    else:
        print("El caso test 4 incorrect3 no funciona")

    ### CASO TEST 5 ###
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    if es_cuadrada(incorrect4):
        print("El caso test 5 incorrect4 funciona")
    else:
        print("El caso test 5 incorrect4 no funciona")

    ### CASO TEST 6 ###
    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    if es_cuadrada(incorrect5):
        print("El caso test 6 incorrect5 funciona")
    else:
        print("El caso test 6 incorrect5 no funciona")

    ### CASO TEST 7 ###
    irregular = [[1,2,3],
                 [2,3,1]]
    if not es_cuadrada(irregular):
        print("El caso test 7 irregular funciona")
    else:
        print("El caso test 7 irregular no funciona")

    ### CASO TEST 8 ###
    irregular2 = [[1,2,3],
                 [2,3,1],
                 [3,1]]
    if not es_cuadrada(irregular2):
        print("El caso test 8 irregular2 funciona")
    else:
        print("El caso test 8 irregular2 no funciona")
