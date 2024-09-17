# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["5", "-100", "-200", "-300", "-900", "1"],
    ["Cantidad de elementos: ", "Ingresa el elemento 0: ", "Ingresa el elemento 1: ",
    "Ingresa el elemento 2: ", "Ingresa el elemento 3: ","Ingresa el elemento 4: ",
     "[-100, -200, -300, -900, 1]",
     "[-100, -200, -300, -900]",
     "[1]",
     "PARES=4",
     "IMPARES=1",
     "[-900, -300, -200, -100, 1]",
     "1",
     "-900"],
    ["La salida no cumple con el caso de prueba\nSon 4 pares y 1 impar."]
    ),
    # Test case 2
    (
    ["7", "0", "401", "301", "202", "800", "400", "7"],
    ["Cantidad de elementos: ", "Ingresa el elemento 0: ", "Ingresa el elemento 1: ",
    "Ingresa el elemento 2: ", "Ingresa el elemento 3: ","Ingresa el elemento 4: ",
    "Ingresa el elemento 5: ", "Ingresa el elemento 6: ",
     "[0, 401, 301, 202, 800, 400, 7]",
     "[0, 202, 800, 400]",
     "[401, 301, 7]",
     "PARES=4",
     "IMPARES=3",
     "[0, 7, 202, 301, 400, 401, 800]",
     "800",
     "0"],
     ["La salida no cumple con el caso de prueba\nSon 4 pares y 3 impares."]
    ),
    # Test case 3
    (
    ["5", "-1", "100", "-2", "300", "0"],
    ["Cantidad de elementos: ", "Ingresa el elemento 0: ", "Ingresa el elemento 1: ",
    "Ingresa el elemento 2: ", "Ingresa el elemento 3: ","Ingresa el elemento 4: ",
     "[-1, 100, -2, 300, 0]",
     "[100, -2, 300, 0]",
     "[-1]",
     "PARES=4",
     "IMPARES=1",
     "[-2, -1, 0, 100, 300]",
     "300",
     "-2"],
    ["La salida no cumple con el caso de prueba\nSon 4 pares y 1 impar."]
    ),
    # Test case 3
    (
    ["0"],
    ["Cantidad de elementos: "],
    ["La salida no cumple, no se debe desplegar datos de salida"]
    )
    ]
