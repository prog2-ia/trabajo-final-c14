from usuario import Usuario

class UsuarioAdministrador(Usuario):

    def eliminar_playlist(self, usuario, playlist):
        if playlist in usuario._playlists:
            usuario._playlists.remove(playlist)
            print(f"Playlist {playlist.titulo} eliminada del usuario {usuario.nombre}")

    def __str__(self):
        return f"Usuario Administrador: {self.nombre}"

    def __repr__(self):
        return f"UsuarioAdministrador(nombre='{self.nombre}')"