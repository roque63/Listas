def main():
    #escribe tu código abajo de esta línea

    # CODIGO ###############

    # leer, separar, contar, ordenar, max, min-----------------------------
    # Autor: roque@tec.mx

    n = int( input("Cantidad de elementos: ") )

    lista = []
    lista_par = []
    lista_impar = []
    for contador in range(n):
        lista.append(int(input(f"Ingresa el elemento {contador}: ")))
        if lista[contador] %2 == 0:
            lista_par.append( lista[contador] )
        else:
            lista_impar.append( lista[contador] )

    if n > 0:
        print(lista)
        print(lista_par)
        print(lista_impar)
        print(f"PARES={len(lista_par)}")
        print(f"IMPARES={len(lista_impar)}")
        lista.sort( )
        print(lista)
        print(max(lista))
        print(min(lista))




if __name__=='__main__':
    main()
