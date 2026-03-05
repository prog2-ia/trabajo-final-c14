from coleccion_musical import ColeccionMusical

class Album:
    def __init__(self, titulo, artista):
        super().__init__(titulo)
        self.artista = artista

    def mostrar_album(self):
        print(f"Álbum: {self.titulo} - {self.artista}")
        for p in self.pistas:
            print(p.info())