class UsuarioGratis(Usuario):
    LIMITE_PLAYLISTS = 3
    
    def crear_playlist(self, playlist):
        if len(self.playlists) >= self.LIMITE_PLAYLISTS:
            print("Has alcanzado el límite de playlists para usuarios gratis.")
        else:
            super().crear_playlist(playlist)