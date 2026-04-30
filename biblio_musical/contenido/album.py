from contenido.coleccion_musical import ColeccionMusical

class Album(ColeccionMusical):
    """Representa un álbum musical que contiene múltiples pistas."""

    def __init__(self, titulo, artista, año):
        super().__init__(titulo)
        self._artista = artista
        self.año = año

    # MÉTODOS
    def mostrar_album(self):
        """Muestra la información del álbum y sus pistas."""
        print(f"Álbum: {self.titulo} - {self._artista.nombre}")
        for p in self._pistas:
            print(p.info())

    def reproducir(self):
        """Reproduce todas las pistas del álbum (polimorfismo)."""
        print(f" Reproduciendo álbum: {self.titulo}")
        for pista in self._pistas:
            pista.reproducir()

    def __str__(self):
        return f"Álbum: {self.titulo} - {self._artista.nombre} ({len(self._pistas)} pistas)"

    def __repr__(self):
        return f"Album(titulo='{self.titulo}', artista='{self._artista.nombre}', pistas={len(self._pistas)})"