from coleccion_musical import ColeccionMusical

class Playlist(ColeccionMusical):
    def __init__(self, titulo, estado_animo):
        super().__init__(titulo)
        self.estado_animo = estado_animo

    def filtrar_por_estado(self):
        resultado = []
        for p in self.pistas:
            if p.estado_animo == self.estado_animo:
                resultado.append(p)
        return resultado

    def mostrar_playlist(self):
        print(f"Playlist: {self.titulo}")
        for p in self.pistas:
            print(p.info())