from playlist import Playlist

class PlaylistPublica(Playlist):

    def mostrar_playlist(self):
        print(f"Playlist pública: {self.titulo}")

        if not self.pistas:
            print("No hay pistas en la playlist.")
            return

        for p in self.pistas:
            print(p.info())