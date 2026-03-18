from usuario import Usuario

class UsuarioGratis(Usuario):
    limite_playlists = 3
    
    def crear_playlist(self, playlist):
        if len(self._playlists) >= self.limite_playlists:
            raise ValueError("Has alcanzado el límite de playlists para usuarios gratis.")
        else:
            super().crear_playlist(playlist)

    def __str__(self):
        return f"Usuario Gratis: {self.nombre}"

    def __repr__(self):
        return f"UsuarioGratis(nombre='{self.nombre}')"