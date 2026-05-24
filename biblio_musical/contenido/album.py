from .coleccion_musical import ColeccionMusical
from .pista import Pista          

class Album(ColeccionMusical):
    
    """Representa un álbum musical que contiene múltiples pistas."""

    def __init__(self, titulo: str, artista: str, año: int) -> None:
        """
        Inicializa un álbum con un título, artista y año de lanzamiento.

        Args:
            titulo (str): El título del álbum.
            artista (str): El nombre del artista o banda.
            año (int): El año de publicación del álbum.
        """
        super().__init__(titulo)
        self._artista = artista
        self.año = año

    def mostrar_album(self) -> None:
        """
        Muestra la información resumida del álbum.
        
        Imprime por consola el título, año, artista, duración total y la lista de todas las pistas que contiene.
        """
        duracion = self.obtener_duracion_total()
        print(f"Album: {self.titulo} ({self.año}) - {self._artista}")
        print(f"Duracion total: {duracion}")
        print("-" * 20)

        if not self._pistas:
            print("El album no tiene pistas registradas.")
        else:
            pista: "Pista"
            for i, pista in enumerate(self._pistas, 1):
                print(f"{i}. {pista.info()}")

    def obtener_duracion_total(self) -> str:
        """Calcula la duracion en formato MM:SS."""
        total_segundos: int = sum(p.duracion for p in self._pistas)
        minutos: int = total_segundos // 60
        segundos: int = total_segundos % 60
        return f"{minutos}:{segundos:02d}"

    def reproducir(self) -> None:
        """Reproduce todas las pistas del álbum (polimorfismo)."""
        print(f"Reproduciendo album: {self.titulo}")
        pista: "Pista"
        for pista in self._pistas:
            pista.reproducir()

    def __str__(self) -> str:
        """Devuelve una representación del álbum en formato de cadena de texto. """
        return f"Album: {self.titulo} - {self._artista} ({len(self._pistas)} pistas)"

    def __repr__(self) -> str:
        """ Devuelve una representación técnica de album"""
        return f"{self.__class__.__name__}(titulo='{self.titulo}', artista='{self._artista}', pistas={len(self._pistas)})"

    def __lt__(self, otro: object) -> bool:
        """
        Ordena albumes por año.

        Args:
            otro (object): Objeto con el que se va a comparar el álbum actual.

        Returns:
            bool: True si el año de este álbum es menor que el del otro, False en caso contrario.
            NotImplemented: Si el objeto comparado no es una instancia de album.
        """
        if not isinstance(otro, Album):
            return NotImplemented
        return self.año < otro.año

    def __eq__(self, otro: object) -> bool:
        """
        Comprueba si dos albumes son iguales por titulo y artista.

        Args:
            otro (object): Objeto a comparar con el álbum actual.

        Returns:
            bool: True si ambos álbumes coinciden en título y artista, False de lo contrario o si no es un album.
        """
        if not isinstance(otro, Album):
            return False
        return self.titulo == otro.titulo and self._artista == otro._artista