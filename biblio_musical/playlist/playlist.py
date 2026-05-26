from contenido.coleccion_musical import ColeccionMusical
from typing import List, Optional, Iterator

class Playlist(ColeccionMusical):
    """ Representa una colección específica de pistas musicales agrupadas bajo un título y un estado de ánimo común."""

    def __init__(self, titulo: str, estado_animo: str) -> None:
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
    def estado_animo(self, value: str) -> None:
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

    def buscar_pista(self, titulo: str) -> Optional[object]:
        """
        Busca una pista específica dentro de la colección por su título.
            
        Returns:
            El objeto pista si existe, sino devuelve None.
        """
        for p in self._pistas:
            if p.titulo == titulo:
                return p
        return None

    def mostrar_playlist(self) -> None:
        """
        Imprime el título de la playlist seguido de la información 
        detallada de cada pista contenida.
        """
        print(f"Playlist: {self.titulo}")
        for p in self._pistas:
            print(p.info())

    def __str__(self) -> str:
        """ Devuelve una representación de la Playlist en formato de cadena de texto"""
        return f"Playlist: {self.titulo} (Estado de ánimo: {self._estado_animo})"

    def __repr__(self) -> str:
        """ Devuelve una representación técnica del objeto Playlist """
        return f"Playlist(titulo='{self.titulo}', estado_animo='{self._estado_animo}')"
    

    def __add__(self, nueva_pista):
        """
        Sobrecarga del operador +. Crea una nueva playlist combinando las pistas actuales con la nueva pista proporcionada.
            
        Returns:
            Una nueva instancia de Playlist que incluye la pista adicional.
        """
        nueva_playlist = Playlist(self.titulo, self._estado_animo) # Nueva instancia
        nueva_playlist._pistas = self._pistas.copy()
        nueva_playlist._pistas.append(nueva_pista)
        return nueva_playlist

    def __iadd__(self, nueva_pista):
        """
        Sobrecarga del operador +=. Modifica la playlist actual añadiendo una nueva pista a la lista interna.

        Returns:
            La misma instancia de Playlist modificada.
        """
        self._pistas.append(nueva_pista) # Modifica la instancia actual
        return self


    def __getitem__(self, indice):
        """
        Permite el acceso a las pistas por medio de un índice utilizando corchetes [].
        
        Args:
            indice: La posición entera de la pista requerida.
            
        Returns:
            El objeto pista correspondiente al índice.
            
        Raises:
            IndexError: Si el índice está fuera del rango de la lista de pistas.
        """
        try:
            return self._pistas[indice]
        except IndexError:
            raise IndexError(f"La pista en el índice {indice} no existe en esta playlist.")
        

    def __iter__(self) -> Iterator:
        """Permite que el objeto Playlist sea iterable """
        return iter(self._pistas)