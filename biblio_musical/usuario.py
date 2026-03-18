class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.playlists = []

    def crear_playlist(self, playlist):
        self.playlists.append(playlist)

    def mostrar_playlists(self):
        for p in self.playlists:
            print(p.nombre)

    def __str__(self):
        return f"Usuario: {self.nombre}"

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}')"