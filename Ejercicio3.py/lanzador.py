# Importamos la clase 'MagiaNumerica' desde el módulo 'procesador_magia'
from procesador_magia import MagiaNumerica

# Definimos la función principal 'ejecutar'
def ejecutar():
    # Creamos una lista de datos numéricos
    datos = [1, 2, 3, 4, 5, 6, 2, 4, 8, 9, 10]
    
    # Instanciamos un objeto de la clase 'MagiaNumerica' con los datos
    magia = MagiaNumerica(datos)
    
    # Llamamos al método 'procesar' para realizar operaciones sobre los datos
    magia.procesar()
    
    # Llamamos al método 'mostrar_resultado' para mostrar los resultados procesados
    magia.mostrar_resultado()
