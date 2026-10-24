# Guía para completar las 4 actividades y reunir evidencias reales

> Esta carpeta contiene el proyecto **correcto y funcionando**. Aún tienes que crear TU repositorio, hacer TUS commits, obtener TUS ejecuciones de Actions y tomar TUS capturas.

## 1) Preparar y verificar (Actividad 1)

1. Descomprime el ZIP y abre `SistemaCalificaciones` en Visual Studio Code.
2. Desde la terminal, ejecuta `python --version`, `git --version` y `python main.py`.
3. Como ejemplo, escribe: `Ana`, `8`, `9`, `10`: resultado esperado `9.00` y `APROBADO`.
4. Ejecuta las pruebas: `python -m unittest discover -s tests -p "test_*.py" -v`.
5. Captura la estructura y la terminal con el programa funcionando.

## 2) Registrar cinco commits significativos (Actividad 2)

Antes de empezar, edita `README.md` para sustituir tu nombre y, cuando exista, el enlace del repositorio. En una terminal ubicada en `SistemaCalificaciones`, ejecuta:

```bash
git init -b main
git config user.name "TU NOMBRE"
git config user.email "TU CORREO DE GIT"

# Commit 1: programa funcional
git add main.py calificaciones.py
git commit -m "feat: implementa calculo de promedio y resultado"

# Commit 2: pruebas unitarias
git add tests/test_calificaciones.py
git commit -m "test: agrega ocho pruebas automatizadas"

# Commit 3: documentacion principal
git add README.md
git commit -m "docs: documenta objetivo, herramientas y ejecucion"

# Commit 4: integracion continua
git add .github/workflows/ci.yml
git commit -m "ci: configura verificacion en GitHub Actions"

# Commit 5: orden del repositorio y guia
git add .gitignore evidencias/LEEME.txt GUIA_PASO_A_PASO.md
git commit -m "chore: organiza archivos y evidencias"

git log --oneline
```

**Importante:** solo utiliza `git config` local si todavía no tenías nombre/correo configurados. Usa el correo asociado a tus commits de GitHub para que se atribuyan a tu cuenta. Cada commit agrupa un cambio de propósito distinto.

En https://github.com/new crea un repositorio **vacío** llamado `SistemaCalificaciones` (sin marcar README, .gitignore o licencia). En tu terminal ejecuta, sustituyendo el nombre de usuario:

```bash
git remote add origin https://github.com/TU_USUARIO/SistemaCalificaciones.git
git push -u origin main
```

GitHub puede solicitarte autenticación desde el navegador o una credencial segura; **no uses tu contraseña normal como token**.

Abre tu repositorio, entra al historial de commits y toma una captura real donde se distingan los cinco mensajes.

## 3) Integración continua (Actividad 3)

1. En el repositorio, abre `.github/workflows/ci.yml` y captura su contenido.
2. Entra a la pestaña **Actions**.
3. Selecciona el flujo «Pruebas automaticas del sistema de calificaciones».
4. Después del `push`, debería existir una ejecución. Abre el trabajo `verificar-proyecto`.
5. Si las ocho pruebas pasan, aparecerá el resultado exitoso. Toma una captura donde se vean la ejecución, el estado verde y las pruebas.
6. Si no aparece el flujo, revisa que el archivo esté en `.github/workflows/ci.yml`, que el `push` haya llegado y que Actions esté habilitado en el repositorio.

## 4) Fallo intencional y corrección (Actividad 4)

Antes de modificar, conserva la evidencia verde inicial.

1. Abre `calificaciones.py` y busca:

```python
return round(sum(calificaciones) / 3, 2)
```

2. **Solo para demostrar el error** cambia a:

```python
return round(sum(calificaciones) / 2, 2)
```

3. Guarda y sube el error con su propio commit:

```bash
git add calificaciones.py
git commit -m "test: introduce error controlado en el promedio"
git push
```

4. En **Actions**, abre la ejecución fallida y captura el indicador rojo y el detalle de `AssertionError`.
5. Corrige el divisor a `/ 3` y sube la corrección:

```bash
git add calificaciones.py
git commit -m "fix: corrige divisor del promedio y recupera pruebas"
git push
```

6. Revisa la nueva ejecución verde y toma una captura de la recuperación. Al final, deben existir **al menos 7 commits** (5 iniciales, 1 con fallo y 1 con corrección).

## 5) Completar el PDF de la entrega

El PDF y el archivo editable DOCX tienen marcadores de posición. En el DOCX completa tu nombre, materia, grupo, fecha, versiones locales (`python --version`, `git --version`, versión de VS Code) y pega la URL real. Sustituye cada marcador de evidencia con las capturas que tomaste **en tu propio repositorio**. Exporta tu versión final a PDF.

**Capturas requeridas recomendadas:**

1. Árbol de archivos en VS Code.
2. Ejecución del programa con resultado.
3. Historial con 5 o más commits.
4. YAML del flujo CI.
5. Ejecución verde inicial.
6. Ejecución roja tras el commit del error.
7. Detalle del error (`AssertionError`).
8. Ejecución verde posterior al commit de corrección.

Nunca inventes ni reutilices capturas de otros proyectos.
