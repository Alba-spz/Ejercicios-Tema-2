# Se importan las clases Galaxia y Estrella desde sus respectivos módulos
from Galaxia import Galaxia
from Estrella import Estrella

# Se define la función principal para ejecutar la simulación
def ejecutar_simulacion():
        # Se crea una instancia de la clase Galaxia
        galaxia = Galaxia()

        # Crear instancias de estrellas con sus respectivas coordenadas y masa
        estrella_a = Estrella(2, 3, 1)  # Estrella en posición (2, 3) con masa 1
        estrella_b = Estrella(4, 4, 4)  # Estrella en posición (4, 4) con masa 4
        estrella_c = Estrella(-3, -1, 0)  # Estrella en posición (-3, -1) con masa 0

        # Se agregan las estrellas creadas a la galaxia
        galaxia.agregar_estrella(estrella_a)
        galaxia.agregar_estrella(estrella_b)
        galaxia.agregar_estrella(estrella_c)

        # Se retorna la galaxia con las estrellas agregadas
        return galaxia
