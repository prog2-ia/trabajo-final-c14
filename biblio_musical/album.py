from coleccion_musical import ColeccionMusical

class Album(ColeccionMusical):
    """Representa un álbum musical que contiene múltiples pistas."""

    def __init__(self, titulo, artista):
        super().__init__(titulo)
        self._artista = artista

    # MÉTODOS
    def mostrar_album(self):
        """Muestra la información del álbum y sus pistas."""
        print(f"Álbum: {self._nombre} - {self._artista}")
        for p in self._pistas:
            print(p.info())

    def reproducir(self):
        """Reproduce todas las pistas del álbum (polimorfismo)."""
        print(f" Reproduciendo álbum: {self._nombre}")
        for pista in self._pistas:
            pista.reproducir()

    def __str__(self):
        return f"Álbum: {self._nombre} - {self._artista} ({len(self._pistas)} pistas)"

    def __repr__(self):
        return f"Album(titulo='{self._nombre}', artista='{self._artista}', pistas={len(self._pistas)})"