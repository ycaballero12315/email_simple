# Guía UV - Instalacion y Uso

## Instalacion (sin privilegios administrativos)

1. Descargar uv desde: https://github.com/astral-sh/uv/releases

2. Agregar al PATH del usuario (PowerShell):
```powershell
setx PATH "$($env:PATH);C:\ruta\completa\a\uv\"
```
> **Nota**: Apuntar a la carpeta, no al .exe que esta dentro

3. Reiniciar PowerShell y verificar:
```powershell
uv --version
```

## Configuración de entorno virtual
```powershell
uv init
uv python pin 3.14
uv add -r requirements.txt
uv lock  # Opcional si no se creó automáticamente
```

## Producción
```powershell
uv sync --frozen
```
> **frozen**: Garantiza que se use exactamente lo versionado

## Comandos útiles

Eliminar entorno virtual:
```powershell
rmdir -r .venv
```