class Artista:
    """Representa un artista musical con una colección de álbumes."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._albums = []

    def agregar_album(self, album) -> None:
        """Añade un album"""
        if album not in self._albums:
            self._albums.append(album)
            # Actualizamos el atributo del album para que apunte a este artista
            album._artista = self 
        else:
            print(f"El album '{album.titulo}' ya esta en la coleccion.")

    def buscar_album(self, titulo: str):
        for a in self._albums:
            if a.titulo == titulo:
                return a
        return None

    def mostrar_albums(self) -> None:
        """Muestra todos los álbumes del artista."""
        print(f"Artista: {self.nombre}")
        for a in sorted(self._albums):
            print(a)

    def total_pistas(self) -> int:
        """Calcula cuantas pistas tiene el artista en total."""
        return sum(len(a._pistas) for a in self._albums)

    def reproducir(self) -> None:
        """Reproduce todos los álbumes del artista (polimorfismo)."""
        print(f" Escuchando al artista: {self.nombre}")
        for album in self._albums:
            album.reproducir()

    def __str__(self) -> str:
        return f"Artista: {self.nombre} ({len(self._albums)} álbumes)"

    def __repr__(self) -> str:
        return f"Artista(nombre='{self.nombre}', albums={len(self._albums)})"