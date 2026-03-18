from playlist import Playlist

class PlaylistPublica(Playlist):

    def mostrar_playlist(self):
        print(f"Playlist pública: {self.titulo}")

        if not self.pistas:
            print("No hay pistas en la playlist.")
            return

        for p in self.pistas:
            print(p.info())

    def __str__(self):
        return f"Playlist pública: {self.titulo} (Estado de ánimo: {self.estado_animo})"
    
    def __repr__(self):
        return f"Playlist(titulo='{self.titulo}', estado_animo='{self.estado_animo}')"