# Importamos la función 'magia_numerica' desde el módulo 'lanzador'
from lanzador import magia_numerica

# Verificamos si el archivo se está ejecutando como programa principal
if __name__ == "__main__":
    # Definimos una lista de datos numéricos
    datos = [1, 2, 3, 4, 5, 6, 2, 4, 8, 9, 10]
    # Llamamos a la función 'magia_numerica' pasando la lista de datos como argumento
    magia_numerica(datos)

