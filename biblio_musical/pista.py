# CLASE PISTA 
from elemento_musical import ElementoMusical

class Pista(ElementoMusical):
    total_pistas = 0  # atributo de clase

    def __init__(self, titulo, artista, genero, duracion, estado_animo=None, calidad=None, favorita=False):
        super().__init__(titulo, artista, genero, duracion)
        self.estado_animo = estado_animo
        self.calidad = calidad
        self.favorita = favorita
        Pista.total_pistas += 1

    def marcar_favorita(self): 
        self.favorita = True 

    def quitar_favorita(self): 
        self.favorita = True

    def info(self):
        return f"{self.artista} - {self.titulo} ({self.genero}) [{self.duracion}s]"

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas

    @staticmethod
    def duracion_valida(duracion):
        return duracion > 0
    