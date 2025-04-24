# Se importa la función ejecutar_simulacion desde el módulo lanzador
from lanzador import ejecutar_simulacion

# Se define la función principal del programa
def main():
    # Se ejecuta la simulación para obtener la galaxia
    galaxia = ejecutar_simulacion()

    # Se muestran las estrellas registradas en la galaxia
    print("🌌 Estrellas registradas:")
    for estrella in galaxia.mostrar_estrellas():
        print("  ", estrella)

    # Se muestra la clasificación de las estrellas por galaxia
    print("\n🛰 Clasificación por galaxia:")
    for estrella, nombre in galaxia.clasificar_estrellas():
        print(f"  {estrella} → {nombre}")

    # Se muestran las distancias calculadas entre las estrellas
    print("\n📏 Distancias entre estrellas:")
    for e1, e2, distancia in galaxia.calcular_distancias():
        print(f"  {e1} ↔ {e2} = {distancia:.2f}")

    # Se determina y muestra la estrella más lejana del origen
    mas_lejana = galaxia.estrella_mas_lejana()
    if mas_lejana:
        print(f"\n🌠 La estrella más lejana del origen es: {mas_lejana} con una distancia de {mas_lejana.distancia_origen():.2f}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
