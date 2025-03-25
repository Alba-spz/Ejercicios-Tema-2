def magia_numerica(lista_original):
    # 1. Eliminar duplicados usando set, luego volver a lista
    lista_sin_duplicados = list(set(lista_original))
    
    # 2. Ordenar de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    
    # 3. Eliminar números impares
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]
    
    # 4. Sumar todos los números que quedan
    suma = sum(lista_pares)
    
    # 5. Colocar esta suma como primer elemento
    nueva_lista = [suma] + lista_pares
    
    # Verificación
    verificacion = sum(nueva_lista[1:]) == nueva_lista[0]
    
    # Imprimir resultados
    print("Lista original: ", lista_original)
    print("Lista transformada: ", nueva_lista)
    print("¿La suma de los elementos desde el segundo es igual al primero?", verificacion)

# Ejemplo de uso
magia_numerica([1, 2, 3, 4, 5, 6, 2, 4, 8, 9, 10])