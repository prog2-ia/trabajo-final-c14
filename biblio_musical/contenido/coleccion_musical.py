from .contenido import Contenido
from servicios.estadistica import Estadistica

class ColeccionMusical(Contenido):
    """Agrupa múltiples pistas musicales."""

    def __init__(self, titulo):
        super().__init__(titulo)
        self._pistas = []

    def agregar_pista(self, pista):
        """Añade una pista a la coleccion."""
        if pista not in self._pistas:
            self._pistas.append(pista)
        else:
            print("La pista ya se encuentra en la coleccion.")

    def eliminar_pista(self, pista):
        """Elimina una pista si existe en la lista."""
        try:
            self._pistas.remove(pista)
        except ValueError:
            print("La pista no existe en esta coleccion.")

    def duracion_total(self):
        return Estadistica.duracion_total(self._pistas)

    @property
    def total_pistas(self):
        return len(self._pistas)

    def reproducir(self):
        """Reproduce todas las pistas de la coleccion."""
        print(f"Reproduciendo coleccion: {self.titulo}")
        for pista in self._pistas:
            # Polimorfismo
            pista.reproducir()

    
    def __len__(self):
        """Permite usar len(objeto_coleccion)."""
        return self.total_pistas

    def __iter__(self):
        """Permite iterar directamente sobre la coleccion."""
        for pista in self._pistas:
            yield pista

    def __getitem__(self, indice):
        """Permite acceder a pistas por indice: coleccion[0]."""
        return self._pistas[indice]

    def __str__(self):
        return f"Colección: {self.titulo} ({len(self._pistas)} pistas)"

    def __repr__(self):
        return f"ColeccionMusical(titulo='{self.titulo}', pistas={len(self._pistas)})"