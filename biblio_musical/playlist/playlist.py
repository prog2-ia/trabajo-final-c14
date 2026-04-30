from coleccion_musical import ColeccionMusical
from typing import List, Optional

class Playlist(ColeccionMusical):
    """ Representa una colección específica de pistas musicales agrupadas bajo un título y un estado de ánimo común."""

    def __init__(self, titulo: str, estado_animo: str):
        """
        Inicializa una nueva Playlist.
        
        Args:
            titulo: El nombre descriptivo de la lista.
            estado_animo: La etiqueta emocional asociada (ej. 'Relajado', 'Enérgico').
        """
        super().__init__(titulo)
        self._estado_animo = estado_animo

    @property
    def estado_animo(self) -> str:
        """Obtiene el estado de ánimo actual de la playlist."""
        return self._estado_animo

    @estado_animo.setter
    def estado_animo(self, value: str):
        """Permite modificar la etiqueta de estado de ánimo."""
        self._estado_animo = value

    def filtrar_por_estado(self) -> List:
        """
        Filtra las pistas dentro de la playlist que coincidan exactamente con el estado de ánimo de la propia lista.
        
        Returns:
            Una lista de objetos pista que comparten el mismo estado de ánimo.
        """
        resultado = []
        for p in self._pistas:
            # Se asume que cada objeto pista tiene un atributo estado_animo
            if p.estado_animo == self._estado_animo:
                resultado.append(p)
        return resultado

    def buscar_pista(self, titulo) -> Optional[object]:
        """
        Busca una pista específica dentro de la colección por su título.
            
        Returns:
            El objeto pista si existe, sino devuelve None.
        """
        for p in self._pistas:
            if p.titulo == titulo:
                return p
        return None

    def mostrar_playlist(self):
        """
        Imprime el título de la playlist seguido de la información 
        detallada de cada pista contenida.
        """
        print(f"Playlist: {self.titulo}")
        for p in self._pistas:
            print(p.info())

    def __str__(self) -> str:
        return f"Playlist: {self.titulo} (Estado de ánimo: {self._estado_animo})"

    def __repr__(self) -> str:
        return f"Playlist(titulo='{self.titulo}', estado_animo='{self._estado_animo}')"