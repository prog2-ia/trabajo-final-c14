from usuarios.usuario import Usuario

class UsuarioAdministrador(Usuario):
    """Subclase de Usuario que posee privilegios de gestión global  """

    def eliminar_playlist(self, usuario: Usuario, playlist: object):
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

    def __str__(self):
        return f"Usuario Administrador: {self.nombre}"

    def __repr__(self):
        return f"UsuarioAdministrador(nombre='{self.nombre}')"