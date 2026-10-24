"""Interfaz de consola del Sistema de Control de Calificaciones."""

from calificaciones import calcular_promedio, obtener_estado


def main():
    print("=== SISTEMA DE CALIFICACIONES ===")
    nombre = input("Nombre del alumno: ").strip()

    if not nombre:
        print("Error: Debes ingresar el nombre del alumno.")
        return

    try:
        calificaciones = [
            float(input(f"Calificación {i} (0 a 10): "))
            for i in range(1, 4)
        ]
        promedio = calcular_promedio(calificaciones)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print("\n--- RESULTADOS ---")
    print(f"Alumno: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {obtener_estado(promedio)}")


if __name__ == "__main__":
    main()
