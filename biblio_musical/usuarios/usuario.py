from datetime import datetime
from typing import List, Optional

class Usuario:
    """Gestiona la información personal del usuario, la fecha de registro y las playlists sociadas."""

    def __init__(self, nombre: str, email: str, edad: int, direccion: str):
        """
        Nuevo usuario con sus datos básicos.
        
        Args:
            nombre: Nombre del usuario
            email: Correo electrónico
            edad: Edad
            direccion: Dirección
        """
        self._nombre = nombre
        self._email = email
        self._edad = edad
        self._direccion = direccion
        self._fecha_registro = datetime.now()
        self._playlists: List = []

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        """Actualiza el nombre del usuario."""
        self._nombre = value

    @property
    def email(self) -> str:
        """Obtiene el correo electrónico."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Actualiza el correo electrónico."""
        self._email = value

    @property
    def edad(self) -> int:
        """Obtiene la edad actual."""
        return self._edad

    @edad.setter
    def edad(self, value: int):
        """Actualiza la edad solo si el valor es un número positivo."""
        if value > 0:
            self._edad = value

    @property
    def direccion(self) -> str:
        """Obtiene la dirección física."""
        return self._direccion

    @direccion.setter
    def direccion(self, value: str):
        """Actualiza la dirección física."""
        self._direccion = value

    @property
    def fecha_registro(self) -> datetime:
        """Obtiene la fecha y hora en que se creó el usuario (Solo lectura)."""
        return self._fecha_registro

    #Gestión de Playlists

    def crear_playlist(self, playlist):
        """Añade una nueva lista de reproducción a la colección del usuario."""
        self._playlists.append(playlist)

    def eliminar_playlist(self, playlist):
        """Elimina una lista de reproducción específica si existe en la colección."""
        if playlist in self._playlists:
            self._playlists.remove(playlist)

    def buscar_playlist(self, titulo: str) -> Optional[object]:
        """
        Busca una playlist por su título

        Returns:
            El objeto playlist si se encuentra, de lo contrario None.
        """
        for p in self._playlists:
            if p.titulo == titulo:
                return p
        return None

    def mostrar_playlists(self):
        """Imprime en consola los títulos de todas las playlists del usuario."""
        for p in self._playlists:
            print(p.titulo)

    def __str__(self):
        return f"Usuario: {self._nombre} ({self._email}, {self._edad} años, {self._direccion})"

    def __repr__(self):
        return f"Usuario(nombre='{self._nombre}', email='{self._email}', edad={self._edad}, direccion='{self._direccion}')"