from playlist import Playlist

class PlaylistPublica(Playlist):
    """Hereda toda la estructura de Playlist y especializa la forma en que se visualiza el contenido """

    def mostrar_playlist(self):
        """ Imprime en consola """
        print(f"Playlist pública: {self.titulo}")

        # Validación de contenido para evitar errores de iteración
        if not self._pistas:
            print("No hay pistas en la playlist.")
            return

        # Itera y muestra la información de cada objeto Pista
        for p in self._pistas:
            print(p.info())

    def __str__(self) -> str:
        return f"Playlist pública: {self.titulo} (Estado de ánimo: {self.estado_animo})"
    
    def __repr__(self) -> str:
        return f"Playlist(titulo='{self.titulo}', estado_animo='{self.estado_animo}')"