class Album:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.pistas = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def mostrar_album(self):
        print(f"Álbum: {self.nombre}")
        for p in self.pistas:
            print(p.info())