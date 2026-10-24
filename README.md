# Sistema de Control de Calificaciones

## Objetivo

Crear un programa de consola en Python que permita ingresar el nombre de un alumno y tres calificaciones, calcular el promedio y mostrar si aprobó o reprobó. La calificación mínima aprobatoria es **6.0**.

## Herramientas

- Python 3.12 (versión usada en GitHub Actions; también funciona con versiones actuales de Python 3).
- Visual Studio Code (editor, opcional).
- Git y GitHub para control de versiones.
- GitHub Actions para integración continua.
- `unittest` (incluido en Python) para pruebas automatizadas.

## Estructura

```text
SistemaCalificaciones/
├── .github/
│   └── workflows/
│       └── ci.yml
├── evidencias/
│   └── LEEME.txt
├── tests/
│   └── test_calificaciones.py
├── .gitignore
├── calificaciones.py
├── main.py
├── README.md
└── GUIA_PASO_A_PASO.md
```

## Cómo ejecutar

1. Instala Python 3 e identifica la carpeta del proyecto.
2. Abre una terminal en la carpeta `SistemaCalificaciones`.
3. Confirma la instalación con `python --version` (en algunos equipos, `py --version` o `python3 --version`).
4. Ejecuta:

```bash
python main.py
```

5. Escribe el nombre y tres calificaciones entre 0 y 10.

**Ejemplo:** Carlos, 8, 9, 10 → promedio 9.00, APROBADO.

## Ejecutar pruebas automáticas

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Al finalizar deben aparecer **8 pruebas** y `OK`.

## Integración continua

El archivo `.github/workflows/ci.yml` configura GitHub Actions para ejecutarse al hacer `push` o abrir/actualizar un `pull_request`. Comprueba la sintaxis y corre las ocho pruebas de `unittest`.

## Evidencia del fallo controlado

Para la actividad académica, después de obtener una ejecución exitosa, cambia **temporalmente** en `calificaciones.py` el divisor del promedio de `/ 3` a `/ 2`, haz un commit y un `push`. La prueba `test_promedio_correcto` fallará. Captura la pantalla de la ejecución roja y su detalle. Restaura `/ 3`, vuelve a hacer commit y `push`, y captura la ejecución verde posterior. **No entregues el proyecto con el error activado.**

## Autor y repositorio

- Alumno: **[ESCRIBE TU NOMBRE]**
- GitHub: **[PEGA AQUÍ EL ENLACE REAL DE TU REPOSITORIO]**
