class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.albums = []

    def agregar_album(self, album):
        self.albums.append(album)

    def mostrar_albums(self):
        print(f"Artista: {self.nombre}")
        for a in self.albums:
            print(a.nombre)