from .contenido import Contenido  # Importamos la clase base Contenido
from .artista import Artista       # Importamos la clase Artista para usarla como tipo

class ElementoMusical(Contenido):

    """ Representa cualquier cosa que sea música individual -> canciones """

    def __init__(self, titulo: str, artista: "Artista", genero: str, duracion: int):
        """ Llamamos al constructor de la clase padre para inicializar el título """
        super().__init__(titulo)
        self.artista = artista      
        self.genero = genero       
        self.duracion = duracion    

    def info(self) -> str:
        """ Devuelve una cadena con la información completa de la canción """
        return f"{self.artista} - {self.titulo}- {self.genero} ({self.duracion} min)"

    def cambiar_genero(self, nuevo_genero: str):
        """ Permite cambiar el género musical de la canción """
        self.genero = nuevo_genero