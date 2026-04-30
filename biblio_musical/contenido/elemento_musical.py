""" Representa cualquier cosa que sea música individual -> canciones """
from .contenido import Contenido  # Importamos la clase base Contenido

class ElementoMusical(Contenido):
    def __init__(self, titulo, artista, genero, duracion):
        """ Llamamos al constructor de la clase padre para inicializar el título """
        super().__init__(titulo)
        self.artista = artista      
        self.genero = genero       
        self.duracion = duracion    

    def info(self):
        """ Devuelve una cadena con la información completa de la canción """
        return f"{self.artista} - {self.titulo}- {self.genero} ({self.duracion} min)"

    def cambiar_genero(self, nuevo_genero):
        """ Permite cambiar el género musical de la canción """
        self.genero = nuevo_genero