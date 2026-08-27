# pasos para hacer comit al git hub

# ==============================================================================
# GUÍA RÁPIDA: SUBIR UN PROYECTO A GITHUB DESDE VS CODE
# ==============================================================================

# 1. Configurar tu identidad en Git (Solo se hace una vez por computadora)
# Registra tu nombre de usuario y correo para firmar los commits.
git config --global user.name "carlosruizzz"
git config --global user.email "carlos.ruiz8566@alumnos.ung.mx"

# 2. Inicializar el repositorio local (Si no lo has iniciado)
# Crea la carpeta oculta .git para empezar a rastrear cambios.
git init

# 3. Vincular el repositorio remoto de GitHub
# Conecta tu carpeta local con el repositorio en la nube.
git remote add origin https://github.com/carlosruizzz/Analisis26B.git

# 4. Preparar todos los archivos modificados
# El punto (.) indica que se agregan todos los archivos del directorio.
git add .

# 5. Crear el primer guardado (Commit)
# Guarda el estado de tus archivos con un mensaje explicativo.
git commit -m "Primer commit"

# 6. Renombrar la rama principal a 'main'
# Asegura que la rama se llame 'main' en lugar del nombre antiguo 'master'.
git branch -M main

# 7. Subir el código a GitHub
# El argumento '-u' guarda la ruta por defecto para futuros envíos.
git push -u origin main

# ==============================================================================
# FLUJO DE TRABAJO DIARIO (Para subir cambios futuros)
# ==============================================================================
# git add .
# git commit -m "Descripción de los nuevos cambios"
# git push