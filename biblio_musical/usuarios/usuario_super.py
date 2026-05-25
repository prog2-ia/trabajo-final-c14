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

    def verificar_usuario(self, usuario):
        """Da un estado de verificación al perfil de un usuario del sistema."""
        usuario.verificado = True
        print(f"{usuario.nombre} ahora es un usuario verificado")

    def transferir_playlist(self, origen, destino, playlist):
        """Mueve una playlist desde la colección de un usuario de origen hacia el de un usuario de destino."""
        if playlist in origen._playlists:
            origen._playlists.remove(playlist)
            destino._playlists.append(playlist)
            print("Playlist transferida correctamente")

    def acceso_total(self):
        """ Simula la apertura de la consola de comandos del sistema. """
        print("Acceso total al sistema habilitado")

    def tipo_cuenta(self):
        """Identifica la categoría de la cuenta de usuario."""
        return "Cuenta super"


    def __str__(self) -> str:
        """representación en formato de texto del Usuario Super."""
        return f"Usuario Super: {self._nombre}"

    def __repr__(self) -> str:
        """representación técnica del objeto UsuarioSuper."""
        return f"UsuarioSuper(nombre='{self._nombre}')"