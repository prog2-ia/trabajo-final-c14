from abc import ABC, abstractmethod

class Contenido(ABC):
    """Clase abstracta base para cualquier contenido musical."""

    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod
    def reproducir(self):
        """Cada contenido debe definir cómo se reproduce."""
        pass

    def __str__(self):
        return f"Contenido: {self.titulo}"

    def __repr__(self):
        return f"Contenido(titulo='{self.titulo}')"