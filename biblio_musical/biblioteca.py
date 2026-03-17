class Biblioteca:
    """Gestiona todas las pistas y playlists del sistema."""

    def __init__(self):
        self._pistas = []
        self._playlists = []

    def agregar_pista(self, pista):
        """Añade una pista a la biblioteca."""
        self._pistas.append(pista)

    def crear_playlist(self, playlist):
        """Añade una playlist."""
        self._playlists.append(playlist)

    def reproducir_todo(self):
        """Reproduce todo el contenido."""
        print(" Reproduciendo toda la biblioteca")
        for p in self._pistas:
            p.reproducir()

        for pl in self._playlists:
            pl.reproducir()

    def buscar(self, genero=None, artista=None, max_duracion=None,
               estado_animo=None, calidad=None):

        resultados = self._pistas

        if genero is not None:
            resultados = [p for p in resultados
                          if p._genero.nombre.lower() == genero.lower()]

        if artista is not None:
            resultados = [p for p in resultados
                          if p._artista.lower() == artista.lower()]

        if max_duracion is not None:
            resultados = [p for p in resultados
                          if p._duracion <= max_duracion]

        if estado_animo is not None:
            resultados = [p for p in resultados
                          if p._estado_animo and p._estado_animo.lower() == estado_animo.lower()]

        if calidad is not None:
            resultados = [p for p in resultados
                          if p._calidad and p._calidad.lower() == calidad.lower()]

        return resultados


    def __str__(self):
        return f"Biblioteca: {len(self._pistas)} pistas, {len(self._playlists)} playlists"

    def __repr__(self):
        return f"Biblioteca(pistas={len(self._pistas)}, playlists={len(self._playlists)})"