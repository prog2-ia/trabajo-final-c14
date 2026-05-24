from abc import ABC, abstractmethod

class Contenido(ABC):
    """Clase abstracta base para cualquier contenido musical."""

    def __init__(self, titulo: str) -> None:
        """
        Inicializa la clase base abstracta con un título.

        Args:
            titulo (str): El título o nombre del contenido musical.
        """
        self.titulo = titulo

    @abstractmethod
    def reproducir(self) -> None:
        """
        Cada contenido debe definir cómo se reproduce.
        Este método es abstracto y debe ser implementado obligatoriamente por cualquier subclase que herede de Contenido.
        
        """
        pass

    def __str__(self) -> str:
        """Devuelve una representación del contenido en formato de cadena de texto."""
        return f"Contenido: {self.titulo}"

    def __repr__(self) -> str:
        """Devuelve una representación técnica del objeto contenido."""
        return f"Contenido(titulo='{self.titulo}')"