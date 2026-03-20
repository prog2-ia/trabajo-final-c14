=======
# Biblioteca Musical

## Descripción

Este proyecto es un sistema de gestión de biblioteca musical desarrollado en Python utilizando principios de programación orientada a objetos. Permite a los usuarios organizar, gestionar e interactuar con contenido musical (pistas, álbumes y listas de reproducción) mientras soporta diferentes tipos de usuarios con niveles de acceso variados.

## Características Principales

- **Gestión de Usuarios**: Sistema multiusuario con permisos diferenciados (gratuito, premium, administrador)
- **Tipos de Listas de Reproducción**: Tres tipos de playlists (pública, privada, compartida)
- **Organización por Estado de Ánimo**: Clasificación y filtrado de pistas basado en el estado de ánimo
- **Búsqueda Avanzada**: Filtrado por género, artista, duración máxima, estado de ánimo y calidad
- **Estadísticas**: Análisis estadístico de pistas (más larga, más corta, duración total, promedio)
- **Marcado de Favoritos**: Posibilidad de marcar pistas como favoritas
- **Reproducción**: Sistema básico de reproducción con visualización de información
- **Validación**: Validación de entradas para asegurar datos correctos

## Estructura del Proyecto

```
biblio_musical/
├── album.py              # Clase para gestionar álbumes
├── artista.py            # Perfiles de artistas que gestionan álbumes
├── biblioteca.py         # Biblioteca central con capacidades de búsqueda
├── coleccion_musical.py  # Clase base para organizar pistas
├── contenido.py          # Clase base abstracta para contenido musical
├── elemento_musical.py   # Representa pistas individuales
├── estadistica.py        # Utilidades estadísticas
├── genero.py             # Gestión de géneros musicales
├── main.py               # Punto de entrada principal del programa
├── pista.py              # Implementación concreta de pistas
├── playlist.py           # Clase base para playlists
├── playlist_compartida.py # Playlists colaborativas
├── playlist_privada.py   # Playlists privadas
├── playlist_publica.py   # Playlists públicas
├── reproductor.py        # Sistema de reproducción
├── usuario.py            # Clase base para usuarios
├── usuario_administrador.py # Usuarios administradores
├── usuario_gratis.py     # Usuarios gratuitos
├── usuario_premium.py    # Usuarios premium
└── validador.py          # Validación de entradas
```

## Clases Principales

### Elementos Musicales
- **Contenido**: Clase base abstracta con propiedad de título
- **ElementoMusical**: Representa pistas individuales con artista, género, duración, estado de ánimo, calidad y estado de favorito
- **Pista**: Implementación concreta de pistas con contador global

### Colecciones
- **ColeccionMusical**: Clase base para organizar pistas con métodos para agregar/quitar y calcular estadísticas
- **Album**: Colección de pistas agrupadas por artista
- **Playlist**: Clase base con filtrado por estado de ánimo

### Usuarios
- **Usuario**: Clase base con gestión de playlists
- **UsuarioPremium**: Usuarios premium con playlists ilimitadas y descargas
- **UsuarioGratis**: Usuarios gratuitos limitados a 3 playlists
- **UsuarioAdministrador**: Administradores con privilegios de eliminación

### Utilidades
- **Biblioteca**: Gestión central de todas las pistas y playlists
- **Reproductor**: Reproducción simple con visualización
- **Estadistica**: Métodos estáticos para análisis estadístico
- **Validador**: Validación de entradas

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd trabajo-final-c14
   ```

2. Asegúrate de tener Python 3.x instalado en tu sistema.

3. No se requieren dependencias externas adicionales.

## Uso

Ejecuta el programa principal:

```bash
python biblio_musical/main.py
```

El programa creará pistas de ejemplo, las agregará a playlists, mostrará información y realizará análisis estadísticos.

### Ejemplo de Uso Programático

```python
from biblio_musical.pista import Pista
from biblio_musical.playlist import Playlist
from biblio_musical.usuario_premium import UsuarioPremium

# Crear una pista
pista = Pista("Canción Ejemplo", "Artista Ejemplo", "Rock", 180, "Energético", "Alta")

# Crear una playlist
playlist = Playlist("Mi Playlist", "Usuario")

# Agregar pista a la playlist
playlist.agregar_pista(pista)

# Crear usuario premium
usuario = UsuarioPremium("Juan", "juan@email.com")
usuario.agregar_playlist(playlist)

# Mostrar información
print(playlist)
```

## Contribución

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Autoras

María Mestre Sánchez, Sandra Crevillen Contreras.

