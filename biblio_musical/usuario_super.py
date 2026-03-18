from usuario_administrador import UsuarioAdministrador
from usuario_premium import UsuarioPremium

class UsuarioSuper(UsuarioAdministrador, UsuarioPremium):
    def __init__(self, nombre, email, edad, direccion):
        # Llama al __init__ de ambas clases padre
        super().__init__(nombre, email, edad, direccion)

    def gestionar_y_descargar(self, usuario, playlist):
        # Combina eliminar_playlist de Administrador y descargar_playlist de Premium
        self.eliminar_playlist(usuario, playlist)
        self.descargar_playlist(playlist)
        print(f"Usuario super {self.nombre} ha gestionado y descargado la playlist {playlist.titulo}")

    def __str__(self):
        return f"Usuario Super: {self.nombre}"

    def __repr__(self):
        return f"UsuarioSuper(nombre='{self.nombre}')"