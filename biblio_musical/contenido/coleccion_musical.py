from .contenido import Contenido
from servicios.estadistica import Estadistica
from .pista import Pista

class ColeccionMusical(Contenido):
    
    """Agrupa varias pistas musicales."""

    def __init__(self, titulo: str) -> None:
        """
        Inicializa una colección musical con su título y una lista de pistas vacía.

        Args:
            titulo (str): El nombre o título de la colección musical.
        """
        super().__init__(titulo)
        self._pistas = []

    def agregar_pista(self, pista: Pista) -> None:
        """Añade una pista a la coleccion."""
        if pista not in self._pistas:
            self._pistas.append(pista)
        else:
            print("La pista ya se encuentra en la coleccion.")

    def eliminar_pista(self, pista : Pista) -> None:
        """Elimina una pista si existe en la lista."""
        try:
            self._pistas.remove(pista)
        except ValueError:
            print("La pista no existe en esta coleccion.")

    def duracion_total(self) -> int:
        """ Calcula la duración total de la colección con  el servicio de estadística."""
        return Estadistica.duracion_total(self._pistas)

    @property
    def total_pistas(self) -> int:
        """ Calcula la cantidad de pistas total en la colección."""
        return len(self._pistas)

    def reproducir(self) -> None:
        """Reproduce todas las pistas de la coleccion."""
        print(f"Reproduciendo coleccion: {self.titulo}")
        for pista in self._pistas:
            # Polimorfismo
            pista.reproducir()

    
    def __len__(self) -> int:
        """Permite usar len(objeto_coleccion)."""
        return self.total_pistas

    def __iter__(self):
        """Permite iterar directamente sobre la coleccion."""
        for pista in self._pistas:
            yield pista

    def __getitem__(self, indice: int) -> Pista:
        """Permite acceder a pistas por indice: coleccion[0]."""
        return self._pistas[indice]

    def __str__(self) -> str:
        """ Devuelve una representación de la colección en formato de cadena de texto."""
        return f"Colección: {self.titulo} ({len(self._pistas)} pistas)"

    def __repr__(self) -> str:
        """ Devuelve una representación oficial del objeto ColeccionMusical."""
        return f"ColeccionMusical(titulo='{self.titulo}', pistas={len(self._pistas)})"