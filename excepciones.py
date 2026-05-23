"""
Excepciones personalizadas

Jerarquía:
    BibliotecaError
    ├── PistaNoEncontradaError
    ├── PlaylistNoEncontradaError
    ├── UsuarioNoEncontradoError
    ├── UsuarioYaExisteError
    ├── LimiteAlcanzadoError
    ├── PermisoDenegadoError
    ├── DuracionInvalidaError
    └── PersistenciaError
"""


class BibliotecaError(Exception):
    """Excepción base de todos los errores del sistema."""

    def __init__(self, mensaje: str = "Error en la Biblioteca Musical"):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[BibliotecaError] {self.mensaje}"


class PistaNoEncontradaError(BibliotecaError):
    """Se lanza cuando se busca una pista que no existe."""

    def __init__(self, titulo: str = ""):
        detalle = f"La pista '{titulo}' no existe en la biblioteca." if titulo else "Pista no encontrada."
        super().__init__(detalle)
        self.titulo = titulo

    def __str__(self):
        return f"[PistaNoEncontradaError] {self.mensaje}"


class PlaylistNoEncontradaError(BibliotecaError):
    """Se lanza cuando se busca una playlist que no existe."""

    def __init__(self, titulo: str = ""):
        detalle = f"La playlist '{titulo}' no existe." if titulo else "Playlist no encontrada."
        super().__init__(detalle)
        self.titulo = titulo

    def __str__(self):
        return f"[PlaylistNoEncontradaError] {self.mensaje}"


class DuracionInvalidaError(BibliotecaError):
    """Se lanza cuando la duración de una pista es negativa o cero."""

    def __init__(self, valor=None):
        detalle = (
            f"La duración '{valor}' no es válida. Debe ser un número entero positivo."
            if valor is not None
            else "Duración inválida."
        )
        super().__init__(detalle)
        self.valor = valor

    def __str__(self):
        return f"[DuracionInvalidaError] {self.mensaje}"


class UsuarioNoEncontradoError(BibliotecaError):
    """Se lanza cuando se busca un usuario que no está registrado."""

    def __init__(self, nombre: str = ""):
        detalle = f"El usuario '{nombre}' no está registrado." if nombre else "Usuario no encontrado."
        super().__init__(detalle)
        self.nombre = nombre

    def __str__(self):
        return f"[UsuarioNoEncontradoError] {self.mensaje}"


class UsuarioYaExisteError(BibliotecaError):
    """Se lanza al intentar registrar un usuario con un nombre ya existente."""

    def __init__(self, nombre: str = ""):
        detalle = f"El usuario '{nombre}' ya está registrado." if nombre else "El usuario ya existe."
        super().__init__(detalle)
        self.nombre = nombre

    def __str__(self):
        return f"[UsuarioYaExisteError] {self.mensaje}"


class LimiteAlcanzadoError(BibliotecaError):
    """
    Se lanza cuando un usuario gratuito supera su cuota.
    Puede ser de playlists o de reproducciones diarias.
    """

    def __init__(self, recurso: str = "recurso", limite: int = 0):
        detalle = f"Has alcanzado el límite de {limite} {recurso} para tu tipo de cuenta."
        super().__init__(detalle)
        self.recurso = recurso
        self.limite = limite

    def __str__(self):
        return f"[LimiteAlcanzadoError] {self.mensaje}"


class PermisoDenegadoError(BibliotecaError):
    """Se lanza cuando un usuario intenta realizar una acción que no le corresponde."""

    def __init__(self, accion: str = "", tipo_usuario: str = ""):
        if accion and tipo_usuario:
            detalle = f"El usuario de tipo '{tipo_usuario}' no tiene permiso para '{accion}'."
        else:
            detalle = "Permiso denegado."
        super().__init__(detalle)
        self.accion = accion
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        return f"[PermisoDenegadoError] {self.mensaje}"



class PersistenciaError(BibliotecaError):
    """Se lanza cuando falla la lectura o escritura de un archivo (CSV o pickle)."""

    def __init__(self, ruta: str = "", operacion: str = "acceder a"):
        detalle = (
            f"No se pudo {operacion} el archivo '{ruta}'."
            if ruta
            else "Error de persistencia."
        )
        super().__init__(detalle)
        self.ruta = ruta
        self.operacion = operacion

    def __str__(self):
        return f"[PersistenciaError] {self.mensaje}"
