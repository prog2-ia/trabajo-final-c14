from usuario import Usuario

class UsuarioPremium(Usuario):

    def __init__(self, nombre):
        super().__init__(nombre)

    def descargar_playlist(self, playlist):
        print(f"{self.nombre} ha descargado la playlist {playlist.nombre}")