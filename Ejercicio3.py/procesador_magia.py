class MagiaNumerica:
    def __init__(self, lista_original):
        # Inicializa la clase con la lista original y otras variables necesarias
        self.lista_original = lista_original
        self.lista_sin_duplicados = []  # Lista sin elementos duplicados
        self.lista_ordenada = []        # Lista ordenada en orden descendente
        self.lista_pares = []           # Lista con solo números pares
        self.suma = 0                   # Suma de los números pares
        self.nueva_lista = []           # Nueva lista con la suma y los números pares
        self.verificacion = False       # Verificación de la condición de suma

    def procesar(self):
        # Ejecuta todos los pasos del procesamiento en orden
        self.eliminar_duplicados()
        self.ordenar_desc()
        self.filtrar_pares()
        self.calcular_suma()
        self.insertar_suma()
        self.verificar()
        return self

    def eliminar_duplicados(self):
        # Elimina los elementos duplicados de la lista original
        self.lista_sin_duplicados = list(set(self.lista_original))

    def ordenar_desc(self):
        # Ordena la lista sin duplicados en orden descendente
        self.lista_ordenada = sorted(self.lista_sin_duplicados, reverse=True)

    def filtrar_pares(self):
        # Filtra los números pares de la lista ordenada
        self.lista_pares = [n for n in self.lista_ordenada if n % 2 == 0]

    def calcular_suma(self):
        # Calcula la suma de los números pares
        self.suma = sum(self.lista_pares)

    def insertar_suma(self):
        # Inserta la suma al inicio de la lista de números pares
        self.nueva_lista = [self.suma] + self.lista_pares

    def verificar(self):
        # Verifica si la suma de los elementos desde el segundo coincide con el primero
        self.verificacion = sum(self.nueva_lista[1:]) == self.nueva_lista[0]

    def mostrar_resultado(self):
        # Muestra los resultados del procesamiento
        print("Lista original: ", self.lista_original)
        print("Lista transformada: ", self.nueva_lista)
        print("¿La suma de los elementos desde el segundo es igual al primero?", self.verificacion)
