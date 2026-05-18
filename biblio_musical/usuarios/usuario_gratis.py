from usuarios.usuario import Usuario

class UsuarioGratis(Usuario):
    """ Subclase de Usuario que representa una cuenta con limitaciones """
    limite_playlists = 3
    limite_reproducciones_diarias = 20

    def __init__(self, nombre, email, edad, direccion):
        super().__init__(nombre, email, edad, direccion)
        self._reproducciones_hoy = 0

    def escuchar_cancion(self, cancion):
        if self._reproducciones_hoy >= self.limite_reproducciones_diarias:
            raise ValueError("Has alcanzado el límite diario de reproducciones.")

        self._reproducciones_hoy += 1
        print(f"{self.nombre} está escuchando {cancion.titulo}")

    def ver_anuncios(self):
        print("Mostrando anuncios...")
    
    def crear_playlist(self, playlist):
        """
        Sobrescribe el método de creación para aplicar una lógica de validación de límites.
        
        Args:
            playlist: El objeto de la lista de reproducción que se intenta añadir.
        """
        if len(self._playlists) >= self.limite_playlists:
            raise ValueError("Has alcanzado el límite de playlists para usuarios gratis.")
        else:
            super().crear_playlist(playlist)

    def tipo_cuenta(self): 
        return "Cuenta Gratis"

    def __str__(self) -> str:
        return f"Usuario Gratis: {self.nombre}"

    def __repr__(self) -> str:
        return f"UsuarioGratis(nombre='{self.nombre}')"