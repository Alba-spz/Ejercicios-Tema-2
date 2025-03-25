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