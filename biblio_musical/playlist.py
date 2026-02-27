class Playlist:
    def __init__(self, nombre, estado_animo):
        self.nombre = nombre
        self.estado_animo = estado_animo
        self.pistas = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def duracion_total(self):
        total = 0
        for p in self.pistas:
            total += p.duracion
        return total

    def mostrar(self):
        print(f"Playlist: {self.nombre}")
        for p in self.pistas:
            print(p.info())