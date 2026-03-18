from usuario import Usuario

class UsuarioAdministrador(Usuario):

    def eliminar_playlist(self, usuario, playlist):
        if playlist in usuario.playlists:
            usuario.playlists.remove(playlist)
            print(f"Playlist {playlist.nombre} eliminada del usuario {usuario.nombre}")

    def __str__(self):
        return f"Usuario Administrador: {self.nombre}"

    def __repr__(self):
        return f"UsuarioAdministrador(nombre='{self.nombre}')"