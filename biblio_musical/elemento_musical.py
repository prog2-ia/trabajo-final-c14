# Representa cualquier cosa que sea musica indivual -> canciones
from contenido import Contenido

class ElementoMusical(Contenido):
    def __init__(self, titulo, artista, genero, duracion):
        super().__init__(titulo)
        self.artista = artista
        self.genero = genero
        self.duracion = duracion

    def info_basica(self):
        return f"{self.artista} - {self.titulo}"

    def cambiar_genero(self, nuevo_genero):
        self.genero = nuevo_genero