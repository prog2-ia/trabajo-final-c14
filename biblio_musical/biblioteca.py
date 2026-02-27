class Biblioteca:
    def __init__(self):
        self.pistas = []
        self.playlists = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def crear_playlist(self, playlist):
        self.playlists.append(playlist)

    def buscar(self,
               genero=None,
               artista=None,
               max_duracion=None,
               estado_animo=None,
               calidad=None):

        resultados = self.pistas

        if genero is not None:
            resultados = [p for p in resultados
                          if p.genero.nombre.lower() == genero.lower()]

        if artista is not None:
            resultados = [p for p in resultados
                          if p.artista.lower() == artista.lower()]

        if max_duracion is not None:
            resultados = [p for p in resultados
                          if p.duracion <= max_duracion]

        if estado_animo is not None:
            resultados = [p for p in resultados
                          if p.estado_animo.lower() == estado_animo.lower()]

        if calidad is not None:
            resultados = [p for p in resultados
                          if p.calidad.lower() == calidad.lower()]

        return resultados

   
