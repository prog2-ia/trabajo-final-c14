class Artista:
    """Representa un artista musical con una colección de álbumes."""

    def __init__(self, nombre):
        self._nombre = nombre
        self._albums = []

    def agregar_album(self, album):
        """Añade un álbum al artista."""
        self._albums.append(album)

    def mostrar_albums(self):
        """Muestra todos los álbumes del artista."""
        print(f"Artista: {self._nombre}")
        for a in self._albums:
            print(a)

    def reproducir(self):
        """Reproduce todos los álbumes del artista (polimorfismo)."""
        print(f" Escuchando al artista: {self._nombre}")
        for album in self._albums:
            album.reproducir()

    def __str__(self):
        return f"Artista: {self._nombre} ({len(self._albums)} álbumes)"

    def __repr__(self):
        return f"Artista(nombre='{self._nombre}', albums={len(self._albums)})"