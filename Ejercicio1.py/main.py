import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Estrella({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        # Clasificación simple por cuadrantes galácticos (ejemplo didáctico)
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Andrómeda"
        elif self.x < 0 and self.y >= 0:
            return "Galaxia Vía Láctea"
        elif self.x < 0 and self.y < 0:
            return "Galaxia Sombrero"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra):
        dx = self.x - otra.x
        dy = self.y - otra.y
        dz = self.z - otra.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def distancia_origen(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# 1. Crear estrellas
estrella_a = Estrella(2, 3, 1)
estrella_b = Estrella(4, 4, 4)
estrella_c = Estrella(-3, -1, 0)

# 2. Imprimir estrellas
print(estrella_a)
print(estrella_b)
print(estrella_c)

# 3. Determinar galaxias
print("Galaxia A:", estrella_a.galaxia())
print("Galaxia B:", estrella_b.galaxia())
print("Galaxia C:", estrella_c.galaxia())

# 4. Calcular distancias
print("Distancia A ↔ B:", estrella_a.distancia(estrella_b))
print("Distancia B ↔ C:", estrella_b.distancia(estrella_c))

# 5. Encontrar estrella más lejana del origen
estrellas = [estrella_a, estrella_b, estrella_c]
mas_lejana = max(estrellas, key=lambda e: e.distancia_origen())

print(f"La estrella más lejana del origen es: {mas_lejana} con una distancia de {mas_lejana.distancia_origen()}")