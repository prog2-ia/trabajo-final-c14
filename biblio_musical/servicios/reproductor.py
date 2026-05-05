class Reproductor:
    """Se encarga de la interfaz de reproducción de audio """

    def __init__(self, volumen=50):
        self.volumen = volumen

    def reproducir(self, pista):
        """
        Inicia la simulación de reproducción de una pista musical.
        
        Args:
            pista: Un objeto que debe contar con el método .info() para extraer sus metadatos antes de "sonar".
        """
        # Se invoca el método info() del objeto pista para mostrar 
        # los detalles técnicos (artista, título, duración) al reproducir.
        print(f"Reproduciendo: {pista.info()}")


    def __mul__(self, factor):
        """
        Sobrecarga de multiplicación para ajustar el volumen[cite: 2].
        Ejemplo: reproductor * 1.2 (sube el volumen un 20%)
        """
        if isinstance(factor, (int, float)):
            nuevo_volumen = min(100, self.volumen * factor)
            return Reproductor(nuevo_volumen)
        return NotImplemented

    def __rmul__(self, factor):
        """Permite hacer: 1.2 * reproductor[cite: 2]"""
        return self.__mul__(factor)
    
    def ajustar_volumen_seguro(self, nuevo_volumen):
        """ Convertir y verificar el volumen """
        try:
            volumen_float = float(nuevo_volumen)
            if volumen_float < 0 or volumen_float > 100:
                raise ValueError("El volumen debe estar entre 0 y 100")
        except ValueError as e:
            print(f"Error al ajustar volumen: {e}")
        else:
            self.volumen = volumen_float
            print(f"Volumen ajustado a {self.volumen}")
        finally:
            print(f"Estado actual del reproductor: {self.volumen}% de volumen")