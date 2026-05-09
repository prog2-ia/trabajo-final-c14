from .artista import Artista
from .elemento_musical import ElementoMusical

class Pista(ElementoMusical):

    """Representa una pista musical."""
    
    total_pistas = 0
    def __init__(self, titulo: str, artista: "Artista", genero: str, duracion: int, favorita: bool=False):
        assert isinstance(duracion, (int, float))
        if duracion <= 0:
            raise ValueError("La duración de la pista debe ser mayor a 0")
        super().__init__(titulo, artista, genero, duracion)
        self._favorita = favorita
        Pista.total_pistas += 1


    @property
    def favorita(self) -> bool:
        return self._favorita

    @favorita.setter
    def favorita(self, value: bool):
        self._favorita = value

    def is_favorita(self) -> bool:
        return self._favorita

    def marcar_favorita(self) -> None:
        """Marca la pista como favorita."""
        self._favorita = True

    def quitar_favorita(self) -> None:
        """Quita la pista de favoritas."""
        self._favorita = False

    def reproducir(self) -> None:
        """Reproduce."""
        print(f" Reproduciendo: {self.titulo} - {self.artista}")

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas

    def __str__(self) -> str:
        return f"Pista: {self.titulo} - {self.artista} ({self.duracion}s)"

    def __repr__(self) -> str:
        return f"Pista('{self.titulo}', '{self.artista}', '{self.genero}', {self.duracion})"
    
    def __add__(self, otro) -> "Pista":
        if isinstance(otro, (int, float)):
            return Pista(self.titulo, self.artista, self.genero, self.duracion + otro, self._favorita)
        if isinstance(otro, Pista):
            # Sumamos las duraciones de ambas pistas
            return Pista(self.titulo, self.artista, self.genero, self.duracion + otro.duracion, self._favorita)
        return NotImplemented

    def __radd__(self, otro):
        """Permite la conmutatividad: 30 + pista"""
        return self.__add__(otro)