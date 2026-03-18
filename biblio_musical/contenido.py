from abc import ABC, abstractmethod

class Contenido(ABC):
    """Clase abstracta base para cualquier contenido musical."""

    def __init__(self, titulo):
        self._nombre = titulo

    def mostrar_titulo(self):
        return self._nombre

    @abstractmethod
    def reproducir(self):
        """Cada contenido debe definir cómo se reproduce."""
        pass

    def descripcion(self):
        return f"Contenido: {self._nombre}"

    def __str__(self):
        return f"Contenido: {self._nombre}"

    def __repr__(self):
        return f"Contenido(titulo='{self._nombre}')"