class ProcesadorDialogoZen:
    # Clase para procesar texto con formato específico de introducción y diálogo

    def __init__(self, texto_bruto):
        # Constructor que inicializa el texto original y otras variables
        self.texto_original = texto_bruto  # Texto original sin procesar
        self.texto_limpio = ""  # Texto después de limpiar saltos de línea
        self.introduccion = ""  # Parte de introducción del texto
        self.dialogo = []  # Lista de partes del diálogo

    def limpiar_saltos(self):
        # Método para eliminar saltos de línea del texto original
        self.texto_limpio = self.texto_original.replace('\n', ' ')  # Reemplaza saltos de línea con espacios
        return self  # Devuelve la instancia para permitir encadenamiento

    def separar_partes(self):
        # Método para separar el texto en introducción y diálogo
        partes = self.texto_limpio.split('#')  # Divide el texto en partes usando '#' como separador
        self.introduccion = partes[0].strip().capitalize() + "..."  # Procesa la introducción
        # Procesa cada parte del diálogo, capitalizándola y agregando un punto
        self.dialogo = ['• ' + parte.strip().capitalize() + '.' for parte in partes[1:]]
        return self  # Devuelve la instancia para permitir encadenamiento

    def formatear(self):
        # Método para formatear el texto procesado en una cadena final
        return self.introduccion + '\n' + '\n'.join(self.dialogo)  # Combina introducción y diálogo

    def procesar(self):
        # Método principal que ejecuta todos los pasos de procesamiento
        return self.limpiar_saltos().separar_partes().formatear()  # Encadena los métodos y devuelve el resultado
