from playlist import Playlist

class PlaylistCompartida(Playlist):

    def __init__(self, titulo, estado_animo):
        super().__init__(titulo, estado_animo)
        self.colaboradores = []

    def agregar_colaborador(self, usuario):
        if usuario not in self.colaboradores:
            self.colaboradores.append(usuario)

    def agregar_pista(self, pista, usuario):

        if usuario in self.colaboradores:
            self.pistas.append(pista)
            print(f"{usuario.nombre} añadió {pista.titulo}")
        else:
            print("No tienes permiso para modificar esta playlist.")

    def __str__(self):
        return f"Playlist compartida: {self.titulo} (Estado de ánimo: {self.estado_animo}) (Colaboradores: {len(self.colaboradores)})"

    def __repr__(self):
        return f"PlaylistCompartida(titulo='{self.titulo}', estado_animo='{self.estado_animo}', colaboradores={self.colaboradores})"