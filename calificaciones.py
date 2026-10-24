"""Reglas de negocio del Sistema de Control de Calificaciones."""


def calcular_promedio(calificaciones):
    """Devuelve el promedio de tres notas válidas entre 0 y 10."""
    if len(calificaciones) != 3:
        raise ValueError("Debes proporcionar exactamente tres calificaciones.")

    for calificacion in calificaciones:
        if not isinstance(calificacion, (int, float)) or isinstance(calificacion, bool):
            raise ValueError("Cada calificación debe ser un número.")
        if not 0 <= calificacion <= 10:
            raise ValueError("Las calificaciones deben estar entre 0 y 10.")

    return round(sum(calificaciones) / 3, 2)


def obtener_estado(promedio):
    """Clasifica el promedio conforme al mínimo aprobatorio de 6.0."""
    if not isinstance(promedio, (int, float)) or not 0 <= promedio <= 10:
        raise ValueError("El promedio debe estar entre 0 y 10.")
    return "APROBADO" if promedio >= 6 else "REPROBADO"
