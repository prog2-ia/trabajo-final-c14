# CLASE PISTA 
class Pista:
    total_pistas = 0  # atributo de clase

    def __init__(self, titulo, artista, genero, duracion, estado_animo=None, calidad=None, favorita=False):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.duracion = duracion  # segundos
        self.estado_animo = estado_animo
        self.calidad = calidad
        self.favorita = favorita
        Pista.total_pistas += 1

    def info(self):
        return f"{self.artista} - {self.titulo} ({self.genero}) [{self.duracion}s]"

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas

    @staticmethod
    def duracion_valida(duracion):
        return duracion > 0
    