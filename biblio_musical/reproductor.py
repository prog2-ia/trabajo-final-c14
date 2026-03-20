class Reproductor:
    """Se encarga de la interfaz de reproducción de audio """

    def reproducir(self, pista):
        """
        Inicia la simulación de reproducción de una pista musical.
        
        Args:
            pista: Un objeto que debe contar con el método .info() para extraer sus metadatos antes de "sonar".
        """
        # Se invoca el método info() del objeto pista para mostrar 
        # los detalles técnicos (artista, título, duración) al reproducir.
        print(f"Reproduciendo: {pista.info()}")