from .playlist import Playlist

""" Clase que representa una playlist que puede ser editada por varios usuarios """
class PlaylistCompartida(Playlist):
    def __init__(self, titulo, estado_animo):
        """ Inicializa la playlist compartida
         Llama al constructor de la clase base Playlist """
        super().__init__(titulo, estado_animo)
        self.colaboradores = []  # Lista de usuarios que pueden modificar la playlist

    def agregar_colaborador(self, usuario):
        """ Agrega un usuario a la lista de colaboradores si no está ya """
        if usuario not in self.colaboradores:
            self.colaboradores.append(usuario)

    def agregar_pista(self, pista, usuario):
        """ Permite agregar una pista solo si el usuario es colaborador """
        if usuario in self.colaboradores:
            self._pistas.append(pista)  # Se asume que _pistas viene de Playlist
            print(f"{usuario.nombre} añadió {pista.titulo}")
        else:
            # Mensaje de error si el usuario no tiene permiso
            print("No tienes permiso para modificar esta playlist.")

    def __str__(self):
        """ Representación  de la playlist """
        return f"Playlist compartida: {self.titulo} (Estado de ánimo: {self.estado_animo}) (Colaboradores: {len(self.colaboradores)})"

    def __repr__(self):
        """ Representación oficial del objeto, útil para depuración """
        return f"PlaylistCompartida(titulo='{self.titulo}', estado_animo='{self.estado_animo}', colaboradores={self.colaboradores})"