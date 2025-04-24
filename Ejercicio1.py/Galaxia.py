from Estrella import Estrella  # Importa la clase Estrella desde el archivo Estrella.py

class Galaxia:
    def __init__(self):
        # Inicializa una galaxia con una lista vacía de estrellas
        self.estrellas = []

    def agregar_estrella(self, estrella):
        # Agrega una estrella a la lista de estrellas de la galaxia
        self.estrellas.append(estrella)

    def mostrar_estrellas(self):
        # Devuelve una lista con las representaciones en cadena de las estrellas
        return [str(e) for e in self.estrellas]

    def clasificar_estrellas(self):
        # Devuelve una lista de tuplas con la representación en cadena de cada estrella
        # y su clasificación según el método galaxia() de la clase Estrella
        return [(str(e), e.galaxia()) for e in self.estrellas]

    def calcular_distancias(self):
        # Calcula las distancias entre todas las combinaciones de dos estrellas
        distancias = []
        for i in range(len(self.estrellas)):
            for j in range(i+1, len(self.estrellas)):
                e1, e2 = self.estrellas[i], self.estrellas[j]
                # Agrega una tupla con las representaciones en cadena de las dos estrellas
                # y la distancia entre ellas calculada con el método distancia()
                distancias.append((str(e1), str(e2), e1.distancia(e2)))
        return distancias

    def estrella_mas_lejana(self):
        # Devuelve la estrella más lejana del origen usando el método distancia_origen()
        # Si no hay estrellas, devuelve None
        return max(self.estrellas, key=lambda e: e.distancia_origen()) if self.estrellas else None
