# Texto original en bruto
texto = """un día que el viento soplaba con fuerza #mira cómo se mueve aquella banderola -dijo un 
monje #lo que se mueve es el viento -respondió otro monje# ni las banderolas ni el viento, lo 
que se mueve son vuestras mentes -dijo el maestro"""

# Paso 1: Limpiar saltos de línea
texto_limpio = texto.replace('\n', ' ')

# Paso 2: Separar la introducción del diálogo
partes = texto_limpio.split('#')

# Paso 3: Capitalizar la primera letra de la introducción
introduccion = partes[0].strip().capitalize() + "..."

# Paso 4: Limpiar y formatear las frases del diálogo
dialogo = ['• ' + parte.strip().capitalize() + '.' for parte in partes[1:]]

# Paso 5: Unir todo en el formato deseado
resultado = introduccion + '\n' + '\n'.join(dialogo)

# Mostrar el resultado
print(resultado)