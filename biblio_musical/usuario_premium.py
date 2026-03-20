from usuario import Usuario

class UsuarioPremium(Usuario):
    """ Subclase de Usuario que representa una cuenta con privilegios como la descarga de contenido para su uso sin conexión """

    def __init__(self, nombre: str, email: str, edad: int, direccion: str):
        """
        Inicializa un nuevo UsuarioPremium llamando al constructor de la clase base.
        
        Args:
            nombre: Nombre completo.
            email: email.
            edad: Edad del usuario.
            direccion: Domicilio de facturación o residencia.
        """
        super().__init__(nombre, email, edad, direccion)

    def descargar_playlist(self, playlist):
        """
        Simula la descarga de una lista de reproducción completa al dispositivo.
        
        Args:
            playlist: El objeto de la lista de reproducción que se desea bajar.
        """
        print(f"{self.nombre} ha descargado la playlist {playlist.titulo}")

    def __str__(self):
        return f"Usuario Premium: {self.nombre}"

    def __repr__(self):
        return f"UsuarioPremium(nombre='{self.nombre}')"