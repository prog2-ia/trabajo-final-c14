from datetime import datetime

class Usuario:
    def __init__(self, nombre, email, edad, direccion):
        self._nombre = nombre
        self._email = email
        self._edad = edad
        self._direccion = direccion
        self._fecha_registro = datetime.now()
        self._playlists = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value > 0:
            self._edad = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def fecha_registro(self):
        return self._fecha_registro

    def crear_playlist(self, playlist):
        self._playlists.append(playlist)

    def eliminar_playlist(self, playlist):
        if playlist in self._playlists:
            self._playlists.remove(playlist)

    def buscar_playlist(self, titulo):
        for p in self._playlists:
            if p.titulo == titulo:
                return p
        return None

    def mostrar_playlists(self):
        for p in self._playlists:
            print(p.titulo)

    def __str__(self):
        return f"Usuario: {self._nombre} ({self._email}, {self._edad} años, {self._direccion})"

    def __repr__(self):
        return f"Usuario(nombre='{self._nombre}', email='{self._email}', edad={self._edad}, direccion='{self._direccion}')"