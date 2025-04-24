# Se importa la clase ProcesadorDialogoZen desde el módulo procesador
from procesador import ProcesadorDialogoZen

# Se define la función ejecutar
def ejecutar():
    # Se define el texto que contiene un diálogo zen
    texto = """un día que el viento soplaba con fuerza #mira cómo se mueve aquella banderola -dijo un 
monje #lo que se mueve es el viento -respondió otro monje# ni las banderolas ni el viento, lo 
que se mueve son vuestras mentes -dijo el maestro"""

    # Se crea una instancia de ProcesadorDialogoZen con el texto dado
    procesador = ProcesadorDialogoZen(texto)
    
    # Se llama al método procesar de la instancia para procesar el texto
    resultado = procesador.procesar()
    
    # Se imprime el resultado del procesamiento
    print(resultado)
