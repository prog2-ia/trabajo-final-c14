class Biblioteca:
    def __init__(self):
        self.pistas = []
        self.playlists = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def crear_playlist(self, playlist):
        self.playlists.append(playlist)

    def buscar_por_genero(self, genero):
        resultado = []
        for p in self.pistas:
            if p.genero == genero:
                resultado.append(p)
        return resultado