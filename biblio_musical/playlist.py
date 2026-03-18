from coleccion_musical import ColeccionMusical

class Playlist(ColeccionMusical):
    def __init__(self, titulo,estado_animo):
        super().__init__(titulo)
        self._estado_animo = estado_animo

    @property
    def estado_animo(self):
        return self._estado_animo

    @estado_animo.setter
    def estado_animo(self, value):
        self._estado_animo = value

    def filtrar_por_estado(self):
        resultado = []
        for p in self._pistas:
            if p.estado_animo == self._estado_animo:
                resultado.append(p)
        return resultado

    def buscar_pista(self, titulo):
        for p in self._pistas:
            if p.titulo == titulo:
                return p
        return None

    def mostrar_playlist(self):
        print(f"Playlist: {self.titulo}")
        for p in self._pistas:
            print(p.info())

    def __str__(self):
        return f"Playlist: {self.titulo} (Estado de ánimo: {self._estado_animo})"

    def __repr__(self):
        return f"Playlist(titulo='{self.titulo}', estado_animo='{self._estado_animo}')"
    