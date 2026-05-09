from .playlist import Playlist

class PlaylistPrivada(Playlist):

    """ Clase que representa una playlist privada, accesible solo para su propietario """
    
    def __init__(self, titulo: str, estado_animo: str, propietario: str) -> None:
        """ Inicializa la playlist privada
        # Llama al constructor de la clase base Playlist """
        super().__init__(titulo, estado_animo)
        self.propietario = propietario  # Usuario que tiene acceso exclusivo a la playlist

    def mostrar_playlist(self, usuario: str) -> None:
        """ Permite mostrar la playlist solo si el usuario es el propietario """
        if usuario == self.propietario:
            print(f"Playlist privada: {self.titulo}")
            for p in self._pistas:  # Recorre las pistas de la playlist
                print(p.info())       # Muestra información de cada pista
        else:
            # Mensaje de error si no eres el propietario
            print("No tienes permiso para ver esta playlist.")

    def __str__(self) -> str:
        """ Representación de la playlist privada """
        return f"Playlist privada: {self.titulo} (Estado de ánimo: {self.estado_animo}, propietario='{self.propietario}')"

    def __repr__(self) -> str:
        """ Representación oficial del objeto, útil para depuración """
        return f"PlaylistPrivada(titulo='{self.titulo}', estado_animo='{self.estado_animo}', propietario='{self.propietario}')"