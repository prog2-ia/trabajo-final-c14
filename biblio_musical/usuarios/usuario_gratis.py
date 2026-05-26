from usuarios.usuario import Usuario

class UsuarioGratis(Usuario):
    """ Subclase de Usuario que representa una cuenta con limitaciones """
    limite_playlists = 3
    limite_reproducciones_diarias = 20

    def __init__(self, nombre, email, edad, direccion):
        """
        Inicializa una nueva instancia de un Usuario de modalidad Gratis.
        
        Args:
            nombre: Nombre completo del usuario.
            email: Dirección de correo electrónico de registro.
            edad: Edad cronológica del usuario.
            direccion: Dirección postal del domicilio.
        """
        super().__init__(nombre, email, edad, direccion)
        self._reproducciones_hoy = 0

    def escuchar_cancion(self, cancion):
        """
        Simula la acción de reproducir una canción tras validar que el usuario no
        haya superado su cuota máxima de consumo asignada para el día actual.
            
        Raises:
            ValueError: Si el contador de reproducciones del día iguala o supera el límite permitido.
        """
        if self._reproducciones_hoy >= self.limite_reproducciones_diarias:
            raise ValueError("Has alcanzado el límite diario de reproducciones.")

        self._reproducciones_hoy += 1
        print(f"{self.nombre} está escuchando {cancion.titulo}")

    def ver_anuncios(self):
        """ Simula la interrupción publicitaria obligatoria para las cuentas gratuitas. """
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
        """Identifica la categoría de la cuenta de usuario."""
        return "Cuenta Gratis"

    def __str__(self) -> str:
        """representación en formato de texto del Usuario Gratis."""
        return f"Usuario Gratis: {self.nombre}"

    def __repr__(self) -> str:
        """representación técnica del objeto UsuarioGratis."""
        return f"UsuarioGratis(nombre='{self.nombre}')"