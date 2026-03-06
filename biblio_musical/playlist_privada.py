from playlist import Playlist

class PlaylistPrivada(Playlist):

    def __init__(self, titulo, estado_animo, propietario):
        super().__init__(titulo, estado_animo)
        self.propietario = propietario

    def mostrar_playlist(self, usuario):
        if usuario == self.propietario:
            print(f"Playlist privada: {self.titulo}")
            for p in self.pistas:
                print(p.info())
        else:
            print("No tienes permiso para ver esta playlist.")