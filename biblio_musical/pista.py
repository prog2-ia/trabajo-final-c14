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
        self.favorita = False

    def info(self):
        base_info = super().info()
        extra_info = f" Estado de ánimo: {self.estado_animo}, Calidad: {self.calidad}, Favorita: {'Sí' if self.favorita else 'No'}"
        return base_info + extra_info

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas
    