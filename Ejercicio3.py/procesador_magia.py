class MagiaNumerica:
    def __init__(self, lista_original):
        # Constructor que inicializa la lista original, la lista procesada y un indicador de resultado válido
        self.lista_original = lista_original
        self.lista_procesada = []  # Lista procesada que se generará después
        self.resultado_valido = False  # Indicador de si el resultado cumple la condición

    def procesar(self):
        # Método para procesar la lista original y transformarla según las reglas
        lista = list(set(self.lista_original))  # 1. Eliminar duplicados convirtiendo la lista en un conjunto y luego de vuelta a lista
        lista = sorted(lista, reverse=True)     # 2. Ordenar la lista en orden descendente
        lista = [n for n in lista if n % 2 == 0]  # 3. Filtrar la lista para conservar solo los números pares
        suma = sum(lista)                        # 4. Calcular la suma de todos los números en la lista filtrada
        self.lista_procesada = [suma] + lista    # 5. Crear la lista procesada colocando la suma como el primer elemento
        # Verificar si la suma de los elementos desde el segundo en adelante es igual al primer elemento
        self.resultado_valido = sum(self.lista_procesada[1:]) == self.lista_procesada[0]

    def mostrar_resultado(self):
        # Método para imprimir los resultados del procesamiento
        print("Lista original:", self.lista_original)  # Imprimir la lista original
        print("Lista transformada:", self.lista_procesada)  # Imprimir la lista procesada
        # Imprimir si la suma desde el segundo elemento es igual al primer elemento
        print("¿La suma desde el segundo elemento es igual al primero?:", self.resultado_valido)

    def obtener_resultado(self):
        # Método para obtener los resultados como una tupla
        return self.lista_procesada, self.resultado_valido  # Retorna la lista procesada y el indicador de resultado válido
