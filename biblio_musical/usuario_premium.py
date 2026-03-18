from usuario import Usuario

class UsuarioPremium(Usuario):

    def __init__(self, nombre, email, edad, direccion):
        super().__init__(nombre, email, edad, direccion)

    def descargar_playlist(self, playlist):
        print(f"{self.nombre} ha descargado la playlist {playlist.titulo}")

    def __str__(self):
        return f"Usuario Premium: {self.nombre}"

    def __repr__(self):
        return f"UsuarioPremium(nombre='{self.nombre}')"