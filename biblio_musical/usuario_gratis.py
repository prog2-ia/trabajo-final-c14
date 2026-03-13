from usuario import Usuario

class UsuarioGratis(Usuario):
    limite_playlists = 3
    
    def crear_playlist(self, playlist):
        if len(self.playlists) >= self.limite_playlists:
            raise ValueError("Has alcanzado el límite de playlists para usuarios gratis.")
        else:
            super().crear_playlist(playlist)