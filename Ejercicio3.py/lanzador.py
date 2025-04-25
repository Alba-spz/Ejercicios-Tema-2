# Importamos la clase 'MagiaNumerica' desde el módulo 'procesador_magia'
from procesador_magia import MagiaNumerica

# Definimos la función 'magia_numerica' que toma una lista como argumento
def magia_numerica(lista_original):
    # Creamos una instancia de la clase 'MagiaNumerica' con la lista proporcionada
    procesador = MagiaNumerica(lista_original)
    
    # Llamamos al método 'procesar' para realizar las operaciones necesarias
    procesador.procesar()
    
    # Llamamos al método 'mostrar_resultado' para imprimir el resultado
    procesador.mostrar_resultado()
    
    # Retornamos el resultado obtenido mediante el método 'obtener_resultado'
    return procesador.obtener_resultado()
