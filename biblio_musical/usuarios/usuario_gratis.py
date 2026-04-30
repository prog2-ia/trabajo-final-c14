from usuarios.usuario import Usuario

class UsuarioGratis(Usuario):
    """ Subclase de Usuario que representa una cuenta con limitaciones """
    limite_playlists = 3
    
    def crear_playlist(self, playlist):
        """
        Sobrescribe el método de creación para aplicar una lógica de validación de límites.
        
        Args:
            playlist: El objeto de la lista de reproducción que se intenta añadir.
        """
        if len(self._playlists) >= self.limite_playlists:
            raise ValueError("Has alcanzado el límite de playlists para usuarios gratis.")
        else:
            super().crear_playlist(playlist)

    def __str__(self):
        return f"Usuario Gratis: {self.nombre}"

    def __repr__(self):
        return f"UsuarioGratis(nombre='{self.nombre}')"