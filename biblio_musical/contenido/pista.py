from .artista import Artista
from .elemento_musical import ElementoMusical

class Pista(ElementoMusical):

    """Representa una pista musical."""
    
    total_pistas = 0

    def __init__(self, titulo: str, artista: "Artista", genero: str, duracion: int, favorita: bool=False):
        """
        Inicializa una nueva pista musical con sus atributos y aumenta el contador global.

        Args:
            titulo (str): El título de la pista.
            artista (Artista): El artista que interpreta la pista.
            genero (str): El género musical de la pista.
            duracion (int): La duración de la pista en segundos.
            favorita (bool, opcional): Indica si la pista es favorita. Por defecto es False.

        Raises:
            ValueError: Si la duración de la pista es menor o igual a cero.
        """
        assert isinstance(duracion, (int, float))
        if duracion <= 0:
            raise ValueError("La duración de la pista debe ser mayor a 0")
        super().__init__(titulo, artista, genero, duracion)
        self._reproducciones = 0
        self._favorita = favorita
        Pista.total_pistas += 1


    @property
    def favorita(self) -> bool:
        """ Devuelve True si la pista es favorita, False en caso contrario"""
        return self._favorita

    @favorita.setter
    def favorita(self, value: bool):
        """ Modificador para actualizar el estado de favorita de la pista """
        self._favorita = value

    def is_favorita(self) -> bool:
        """ Comprueba de forma explícita si la pista es favorita."""
        return self._favorita

    def marcar_favorita(self) -> None:
        """Marca la pista como favorita."""
        self._favorita = True

    def quitar_favorita(self) -> None:
        """Quita la pista de favoritas."""
        self._favorita = False

    def reproducir(self) -> None:
        """Reproduce."""
        print(f" Reproduciendo: {self.titulo} - {self.artista}")

    @classmethod
    def cantidad_pistas(cls):
        """ Método de clase que obtiene la cantidad total de todas las pistas instanciadas."""
        return cls.total_pistas

    def __str__(self) -> str:
        """ Devuelve una representación de la pista en formato de cadena de texto"""
        return f"Pista: {self.titulo} - {self.artista} ({self.duracion}s)"

    def __repr__(self) -> str:
        """ Devuelve una representación técnica del objeto pista."""
        return f"Pista('{self.titulo}', '{self.artista}', '{self.genero}', {self.duracion})"
    
    def __add__(self, otro) -> "Pista":
        """
        Permite sumar un entero/flotante o una instancia de otra Pista a la pista actual.
        
        Crea una nueva pista con la suma de las duraciones conservando los demás atributos.

        Args:
            otro (int, float, Pista): El valor numérico en segundos o el objeto Pista a sumar.

        Returns:
            Pista: Una nueva instancia de Pista con la duración acumulada.
            NotImplemented: Si el tipo del operando no está soportado.
        """
        if isinstance(otro, (int, float)):
            return Pista(self.titulo, self.artista, self.genero, self.duracion + otro, self._favorita)
        if isinstance(otro, Pista):
            # Sumamos las duraciones de ambas pistas
            return Pista(self.titulo, self.artista, self.genero, self.duracion + otro.duracion, self._favorita)
        return NotImplemented

    def __radd__(self, otro):
        """Permite la conmutatividad: 30 + pista
        Args:
            otro (int, float): Valor numérico en segundos sumado desde la izquierda.

        Returns:
            Pista: Una nueva instancia de Pista con la duración acumulada.
        """
        return self.__add__(otro)
    
    @property
    def reproducciones(self) -> int:
        """ Obtiene el número de veces que se ha reproducido la pista"""
        return self._reproducciones

    def reiniciar_reproducciones(self) -> None:
        """Restablece el contador interno de reproducciones de la pista a 0."""
        self._reproducciones = 0