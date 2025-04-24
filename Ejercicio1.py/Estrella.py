import math

class Estrella:
    # Constructor de la clase Estrella, inicializa las coordenadas x, y, z
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Método para representar la estrella como una cadena
    def __str__(self):
        return f"Estrella({self.x}, {self.y}, {self.z})"

    # Método para determinar a qué galaxia pertenece la estrella según sus coordenadas
    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Andrómeda"
        elif self.x < 0 and self.y >= 0:
            return "Galaxia Vía Láctea"
        elif self.x < 0 and self.y < 0:
            return "Galaxia Sombrero"
        else:
            return "Galaxia Desconocida"

    # Método para calcular la distancia entre esta estrella y otra estrella
    def distancia(self, otra):
        dx = self.x - otra.x  # Diferencia en el eje x
        dy = self.y - otra.y  # Diferencia en el eje y
        dz = self.z - otra.z  # Diferencia en el eje z
        return math.sqrt(dx**2 + dy**2 + dz**2)  # Fórmula de distancia euclidiana

    # Método para calcular la distancia de la estrella al origen (0, 0, 0)
    def distancia_origen(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)  # Distancia al origen