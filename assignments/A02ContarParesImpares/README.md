![Tec de Monterrey](../../images/logotecmty.png)
# cuenta pares e impares
## Tema: Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.
- El programa ingresa la cantidad de valores a leer de la lista.
- Diseña e implementa un programa que calcule la cantidad de valores pares e impares de los elementos de una lista de números enteros que lee como datos de entrada. 
- Los valores los introduce el usuario uno por uno, se van almacenando en una lista y posteriormente se analizará la lista para calcular cuantos valores pares e impares posee. Consideramos al 0 como par.
- Los valores pares deben almacenarse en una lista y los impares en otra lista.


## Entrada
- Cantidad de valores a ingresar : n
- Leer los n valores enteros, uno en cada renglón, desplegando el mensaje:   __Ingresa el elemento \#:__
- El # indica el indice dentro de la lista del elemento que se va a leer.

## Salida
- Desplegar la lista con todos los valores
- Desplegar la lista de pares 
- Desplegar la lista de impares 
- Desplegar  el número de pares e impares con el siguiente formato: 
- PARES=3 o IMPARES=2 cada uno en un renglón. 
- El desplegado de la salida consiste en la palabra PARES seguida de un = y luego un número que representa el número de pares en la lista; posteriormente la palabra IMPARES, seguida de un = y luego el número que representa el número de impares que hay en la lista. 
- Desplegar la lista con todos los valores ingresados ordenados en forma ascendente
- Desplegar el valor máximo ingresado
- Desplegar el valor mínimo ingresado
Cada mensaje en un renglón y en ese orden.

## Ejemplo de ejecución del programa
```
Cantidad de elementos: 5
Ingresa el elemento 0: 100
Ingresa el elemento 1: 23
Ingresa el elemento 2: 45
Ingresa el elemento 3: 6
Ingresa el elemento 4: 0
[100, 23, 45, 6, 0]
[100, 6, 0]
[23, 45]
PARES=3
IMPARES=2
[0, 6, 23, 45, 100]
100
0
```

## Ejemplo de ejecución del programa

```
Cantidad de elementos: 7
Ingresa el elemento 0: 0
Ingresa el elemento 1: 401
Ingresa el elemento 2: 301
Ingresa el elemento 3: 202
Ingresa el elemento 4: 800
Ingresa el elemento 5: 400
Ingresa el elemento 6: 7
[0, 401, 301, 202, 800, 400, 7]
[0, 202, 800, 400]
[401, 301, 7]
PARES=4
IMPARES=3
[0, 7, 202, 301, 400, 401, 800]
800
0
```


## Ejemplo de ejecución del programa
```
Cantidad de elementos: 0
```

## Ejemplo de ejecución del programa
```
Cantidad de elementos: 5
Ingresa el elemento 0: -100
Ingresa el elemento 1: -200
Ingresa el elemento 2: -300
Ingresa el elemento 3: -900
Ingresa el elemento 4: 1
[-100, -200, -300, -900, 1]
[-100, -200, -300, -900]
[1]
PARES=4
IMPARES=1
[-900, -300, -200, -100, 1]
1
-900

```
**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
