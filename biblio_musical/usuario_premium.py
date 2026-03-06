class UsuarioPremium(Usuario):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.calidad_audio = "alta"

    def descargar_playlist(self, playlist):
        print(f"{self.nombre} ha descargado la playlist {playlist.nombre}")