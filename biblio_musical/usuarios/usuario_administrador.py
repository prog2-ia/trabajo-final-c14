from usuarios.usuario import Usuario

class UsuarioAdministrador(Usuario):
    """Subclase de Usuario que posee privilegios de gestión global  """

    def eliminar_playlist(self, usuario: Usuario, playlist: object) -> None:
        """
        Elimina una playlist de la colección de otro usuario.
        
        Args:
            usuario: La instancia del usuario al que se le desea remover contenido.
            playlist: El objeto de la lista de reproducción que será eliminado.
        """
        if playlist in usuario._playlists:
            usuario._playlists.remove(playlist)
            print(f"Playlist {playlist.titulo} eliminada del usuario {usuario.nombre}")
        else:
            print(f"La playlist no se encuentra en el perfil de {usuario.nombre}")
    
    def banear_usuario(self, usuario):
        usuario.baneado = True
        print(f"{usuario.nombre} ha sido baneado")

    def ver_total_playlists(self, usuario):
        return len(usuario._playlists)
    
    def eliminar_todas_playlists(self, usuario):
        usuario._playlists.clear()

    def __str__(self) -> str:
        return f"Usuario Administrador: {self.nombre}"

    def __repr__(self) -> str:
        return f"UsuarioAdministrador(nombre='{self.nombre}')"
    