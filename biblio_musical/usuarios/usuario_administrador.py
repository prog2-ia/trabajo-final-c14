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
        """
        Restringe el acceso al sistema marcando el estado del usuario como baneado.

        """
        usuario.baneado = True
        print(f"{usuario.nombre} ha sido baneado")

    def ver_total_playlists(self, usuario):
        """ Consulta y devuelve la cantidad de listas de reproducción que posee un usuario específico."""
        return len(usuario._playlists)
    
    def eliminar_todas_playlists(self, usuario):
        """Vacía por completo y de forma irreversible la lista de reproducción de un usuario."""
        usuario._playlists.clear()
    
    def tipo_cuenta(self):
        """Identifica el rol o categoría de privilegios asociados a este tipo de cuenta."""
        return "Cuenta administrador"

    def __str__(self) -> str:
        """representación informal en texto del Administrador."""
        return f"Usuario Administrador: {self.nombre}"

    def __repr__(self) -> str:
        """representación técnica del objeto UsuarioAdministrador."""
        return f"UsuarioAdministrador(nombre='{self.nombre}')"
    