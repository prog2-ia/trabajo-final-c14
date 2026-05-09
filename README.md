# Biblioteca Musical

## Descripción

Sistema de gestión de biblioteca musical desarrollado en Python utilizando principios de **Programación Orientada a Objetos**. Permite organizar, gestionar e interactuar con contenido musical: pistas, álbumes y playlists, con persistencia de datos mediante archivos CSV.

---

## Características Principales

- **Gestión de pistas**: Crear, buscar, reproducir y eliminar pistas musicales
- **Gestión de playlists**: Crear, reproducir y eliminar listas de reproducción con estado de ánimo asociado
- **Géneros dinámicos**: Los géneros no están limitados a una lista fija, al introducir uno nuevo se añade automáticamente
- **Búsqueda flexible**: Filtrado por título, artista o género
- **Estadísticas**: Número de pistas, playlists y duración total de la biblioteca
- **Persistencia CSV**: Los datos se guardan y cargan automáticamente entre sesiones
- **Validación de entradas**: Control de errores en todas las entradas del usuario

---

## Estructura del Proyecto

```
biblio_musical/
├── main.py                          # Punto de entrada y menú interactivo
│
├── contenido/                       # Jerarquía de clases de contenido musical
│   ├── __init__.py
│   ├── contenido.py                 # Clase base abstracta (título)
│   ├── elemento_musical.py          # Extiende Contenido con artista, género, duración
│   ├── pista.py                     # Pista concreta con contador global
│   ├── coleccion_musical.py         # Agrupa pistas (iterable, indexable)
│   ├── album.py                     # Colección agrupada por artista
│   ├── artista.py                   # Perfil de artista con sus álbumes
│   └── genero.py                    # Representa un género musical
│
├── playlist/                        # Tipos de listas de reproducción
│   ├── __init__.py
│   ├── playlist.py                  # Playlist base con estado de ánimo
│   ├── playlist_publica.py          # Playlist accesible por todos
│   ├── playlist_privada.py          # Playlist de uso personal
│   └── playlist_compartida.py       # Playlist colaborativa
│
├── servicios/                       # Lógica de negocio y utilidades
│   ├── __init__.py
│   ├── biblioteca.py                # Gestión central de pistas y playlists
│   ├── estadistica.py               # Métodos estáticos de análisis
│   ├── reproductor.py               # Sistema de reproducción
│   ├── validador.py                 # Validación de entradas
│   └── csv_manager.py               # Lectura y escritura de archivos CSV
│
├── usuarios/                        # Sistema de usuarios (estructura base)
│   ├── __init__.py
│   ├── usuario.py                   # Clase base de usuario
│   ├── usuario_gratis.py            # Usuario con funcionalidad limitada
│   ├── usuario_premium.py           # Usuario con acceso completo
│   ├── usuario_administrador.py     # Administrador con privilegios extra
│   └── usuario_super.py             # Superusuario del sistema
│
└── datos/                           # Archivos CSV generados automáticamente
    ├── pistas.csv
    └── playlists.csv
```

---

## Clases Principales

### Jerarquía de contenido

| Clase | Hereda de | Descripción |
|---|---|---|
| `Contenido` | — | Clase base abstracta con título |
| `ElementoMusical` | `Contenido` | Añade artista, género y duración |
| `Pista` | `ElementoMusical` | Pista concreta con contador global |
| `ColeccionMusical` | `Contenido` | Agrupa pistas, iterable e indexable |
| `Album` | `ColeccionMusical` | Colección agrupada por artista |
| `Playlist` | `ColeccionMusical` | Lista con estado de ánimo asociado |

### Servicios

- **`Biblioteca`**: Gestión central; almacena pistas y playlists, búsqueda y persistencia CSV
- **`Estadistica`**: Métodos estáticos para calcular duración total, promedio, pista más larga/corta
- **`Validador`**: Valida títulos, artistas, duración y géneros
- **`csv_manager`**: Funciones de lectura, escritura, modificación y eliminación en CSV

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/prog2-ia/trabajo-final-c14.git
   cd trabajo-final-c14
   ```

2. Asegúrate de tener **Python 3.x** instalado. No se requieren dependencias externas.

---

## Uso

Ejecuta el programa desde dentro de la carpeta `biblio_musical`:

```bash
cd biblio_musical
python main.py
```

La primera vez que se ejecuta, se crean automáticamente pistas y playlists de ejemplo y se guardan en `datos/`. En siguientes ejecuciones, los datos se cargan desde los CSV.

### Menú interactivo

```
=== MENÚ ===
1.  Ver todas las pistas
2.  Ver todas las playlists
3.  Crear nueva pista
4.  Crear nueva playlist
5.  Agregar pista a playlist
6.  Buscar pistas
7.  Reproducir pista
8.  Reproducir playlist
9.  Estadísticas básicas
10. Eliminar pista
11. Eliminar playlist
0.  Salir
```

### Géneros disponibles por defecto

`Rock`, `Pop`, `Jazz`, `Clásica`, `Electrónica`, `Hip-Hop`, `Reggae`, `Blues`, `Reggaetton`, `Trap`, `Indie`

Al introducir un género que no esté en la lista, se añade automáticamente para esa sesión.

---

## Persistencia de datos

Los datos se guardan en la carpeta `datos/` en formato CSV:

- `pistas.csv` — título, artista, género y duración de cada pista
- `playlists.csv` — título, estado de ánimo y pistas de cada playlist

El guardado se hace automáticamente al crear o eliminar pistas y playlists, y también al salir con la opción `0`.

---

## Autoras

**María Mestre Sánchez** y **Sandra Crevillen Contreras**