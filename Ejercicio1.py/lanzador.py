import math

def distancia(self, otra):
        dx = self.x - otra.x
        dy = self.y - otra.y
        dz = self.z - otra.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

def distancia_origen(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)