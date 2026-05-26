"""
Configura el entorno de ejecución del sistema asegurando que los módulos 
locales sean accesibles, para luego invocar la función principal de control.
"""

import sys
import os
 
# Permite la ejecución del script desde cualquier directorio del sistema.
# Añade la carpeta que contiene a este archivo al inicio de 'sys.path' 
sys.path.insert(0, os.path.dirname(__file__))
 
from main import main
 
if __name__ == "__main__":
    """
    Bloque de ejecución principal.
    
    Asegura que el código interno solo se ejecute si el archivo es lanzado directamente como el script principal, evitando su ejecución accidental 
    si es importado desde otro módulo.
    """
    main()
 
