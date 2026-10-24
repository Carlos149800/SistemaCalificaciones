"""Pruebas que ejecutan tanto la computadora local como GitHub Actions."""

import unittest

from calificaciones import calcular_promedio, obtener_estado


class PruebasCalificaciones(unittest.TestCase):
    def test_promedio_correcto(self):
        self.assertEqual(calcular_promedio([8, 9, 10]), 9.0)

    def test_promedio_con_decimales(self):
        self.assertEqual(calcular_promedio([7, 8, 8]), 7.67)

    def test_aprobado(self):
        self.assertEqual(obtener_estado(6), "APROBADO")

    def test_reprobado(self):
        self.assertEqual(obtener_estado(5.9), "REPROBADO")

    def test_calificacion_negativa(self):
        with self.assertRaises(ValueError):
            calcular_promedio([-1, 8, 9])

    def test_calificacion_superior_a_diez(self):
        with self.assertRaises(ValueError):
            calcular_promedio([11, 8, 9])

    def test_numero_incorrecto_de_calificaciones(self):
        with self.assertRaises(ValueError):
            calcular_promedio([8, 9])

    def test_tipo_incorrecto(self):
        with self.assertRaises(ValueError):
            calcular_promedio(["ocho", 8, 9])


if __name__ == "__main__":
    unittest.main()
