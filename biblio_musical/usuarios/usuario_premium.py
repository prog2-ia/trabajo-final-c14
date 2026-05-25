from usuarios.usuario import Usuario

class UsuarioPremium(Usuario):
    """ Subclase de Usuario que representa una cuenta con privilegios como la descarga de contenido para su uso sin conexión """

    def __init__(self, nombre: str, email: str, edad: int, direccion: str) -> None:
        """
        Inicializa un nuevo UsuarioPremium llamando al constructor de la clase base.
        
        Args:
            nombre: Nombre completo.
            email: email.
            edad: Edad del usuario.
            direccion: Domicilio de facturación o residencia.
        """
        super().__init__(nombre, email, edad, direccion)
        self._favoritos = []


    def agregar_a_favoritos(self, cancion):
        """Añade una canción al listado interno de favoritos del usuario si no se encuentra ya indexada."""
        if cancion not in self._favoritos:
            self._favoritos.append(cancion)

    def mostrar_favoritos(self):
        """ Muestra por consola el título de todas las canciones añadidas a la lista de favoritos. """
        for c in self._favoritos:
            print(c.titulo)

    def escuchar_sin_anuncios(self):
        """ Simula el inicio del flujo de reproducción"""
        print("Reproduciendo música sin anuncios en calidad HD")
    
    def tipo_cuenta(self):
        """Identifica la categoría de la cuenta de usuario."""
        return "Cuenta premium"

    def descargar_playlist(self, playlist):
        """
        Simula la descarga de una lista de reproducción completa al dispositivo.
        
        Args:
            playlist: El objeto de la lista de reproducción que se desea bajar.
        """
        print(f"{self.nombre} ha descargado la playlist {playlist.titulo}")

    def __str__(self):
        """representación en formato de texto del Usuario Premium."""
        return f"Usuario Premium: {self.nombre}"

    def __repr__(self):
        """representación técnica del objeto UsuarioPremium."""
        return f"UsuarioPremium(nombre='{self.nombre}')"