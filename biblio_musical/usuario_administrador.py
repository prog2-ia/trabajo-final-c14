class UsuarioAdministrador(Usuario):

    def eliminar_playlist(self, usuario, playlist):
        if playlist in usuario.playlists:
            usuario.playlists.remove(playlist)
            print(f"Playlist {playlist.nombre} eliminada del usuario {usuario.nombre}")