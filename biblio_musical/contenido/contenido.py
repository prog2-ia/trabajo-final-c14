from abc import ABC, abstractmethod

class Contenido(ABC):
    """Clase abstracta base para cualquier contenido musical."""

    def __init__(self, titulo: str) -> None:
        self.titulo = titulo

    @abstractmethod
    def reproducir(self) -> None:
        """Cada contenido debe definir cómo se reproduce."""
        pass

    def __str__(self) -> str:
        return f"Contenido: {self.titulo}"

    def __repr__(self) -> str:
        return f"Contenido(titulo='{self.titulo}')"