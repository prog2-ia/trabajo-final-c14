from .contenido import Contenido
from servicios.estadistica import Estadistica

class ColeccionMusical(Contenido):
    """Agrupa múltiples pistas musicales."""

    def __init__(self, titulo):
        super().__init__(titulo)
        self._pistas = []

    def agregar_pista(self, pista):
        """Añade una pista a la colección."""
        self._pistas.append(pista)

    def eliminar_pista(self, pista):
        """Elimina una pista si existe."""
        if pista in self._pistas:
            self._pistas.remove(pista)

    def duracion_total(self):
        return Estadistica.duracion_total(self._pistas)

    def total_pistas(self):
        return len(self._pistas)

    def reproducir(self):
        """Reproduce todas las pistas."""
        print(f" Reproduciendo colección: {self.titulo}")
        for pista in self._pistas:
            pista.reproducir()

    def __str__(self):
        return f"Colección: {self.titulo} ({len(self._pistas)} pistas)"

    def __repr__(self):
        return f"ColeccionMusical(titulo='{self.titulo}', pistas={len(self._pistas)})"