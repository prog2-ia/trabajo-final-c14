from usuarios.usuario_administrador import UsuarioAdministrador
from usuarios.usuario_premium import UsuarioPremium

class UsuarioSuper(UsuarioAdministrador, UsuarioPremium):
    """Implementa herencia múltiple para combinar los privilegios de un Administrador y las ventajas de un Usuario Premium"""

    def __init__(self, nombre, email, edad, direccion):
        """Inicializa un UsuarioSuper delegando la creación a las clases padre."""
        super().__init__(nombre, email, edad, direccion)

    def gestionar_y_descargar(self, usuario, playlist):
        """
        Elimina una playlist de un usuario y la descarga
        
        Args:
            usuario: Instancia del usuario al que se le gestionará el contenido.
            playlist: Objeto de la lista de reproducción a procesar.
        """
        # Accion de UsuarioAdministrador
        self.eliminar_playlist(usuario, playlist)
        
        # Accion de UsuarioPremium
        self.descargar_playlist(playlist)
        
        print(f"Usuario super {self.nombre} ha gestionado y descargado la playlist {playlist.titulo}")

    def __str__(self):
        return f"Usuario Super: {self._nombre}"

    def __repr__(self):
        return f"UsuarioSuper(nombre='{self._nombre}')"